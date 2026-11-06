import random
from monster import create_random_monster, ShadowKing
from skill import create_skill
from inventory import use_item
from item import ITEMS
from player import add_xp
from quest import record_monster_victory, complete_boss_quest
from utils import ask, good, warn, bad, info
from game_map import starting_position

def battle(player, final_boss=False):
    monster = ShadowKing() if final_boss else create_random_monster(player["current_map"])
    info(f"\nA {monster.name} appears! Enemy HP: {monster.hp}")
    while monster.is_alive() and player["hp"] > 0:
        print(f"\n{player['name']} HP: {player['hp']}/{player['max_hp']}")
        print(f"{monster.name} HP: {monster.hp}/{monster.max_hp}")
        print("1. Use skill")
        print("2. Use healing item")
        if not final_boss:
            print("3. Run away")
        action = ask("Choose: ")

        if action == "1":
            print("Your skills:")
            for index, name in enumerate(player["skills"], 1):
                cooldown = player["cooldowns"].get(name, 0)
                print(f"{index}. {name} (cooldown: {cooldown})")
            skill_choice = ask("Choose a skill number, or 0 to cancel: ")
            if skill_choice == "0":
                continue
            if not skill_choice.isdigit() or not 1 <= int(skill_choice) <= len(player["skills"]):
                warn("Invalid skill selection.")
                continue
            skill_name = player["skills"][int(skill_choice) - 1]
            if player["cooldowns"].get(skill_name, 0) > 0:
                warn(f"{skill_name} is on cooldown for {player['cooldowns'][skill_name]} more turn(s).")
                continue
            skill = create_skill(skill_name)
            good(skill.use(player, monster))
            player["cooldowns"][skill_name] = skill.cooldown
        elif action == "2":
            old_hp = player["hp"]
            use_item(player)
            if player["hp"] == old_hp:
                continue
        elif action == "3" and not final_boss:
            warn("You escaped from the battle.")
            return "escaped"
        else:
            warn("Invalid battle action.")
            continue

        if not monster.is_alive():
            break

        damage = max(1, monster.attack + random.randint(-2, 2))
        player["hp"] = max(0, player["hp"] - damage)
        bad(f"{monster.name} hits you for {damage} damage.")
        for name in player["cooldowns"]:
            if player["cooldowns"][name] > 0:
                player["cooldowns"][name] -= 1

    if player["hp"] <= 0:
        warn("You were defeated! You wake up in Eldoria Village.")
        player["hp"] = max(1, player["max_hp"] // 2)
        player["gold"] //= 2
        player["current_map"] = "Eldoria Village"
        player["position"] = starting_position("Eldoria Village")
        return "defeat"

    gold, dropped_item = monster.loot()
    player["gold"] += gold
    player["total_monsters_defeated"] += 1
    good(f"You defeated {monster.name}! Rewards: {monster.xp_reward} XP and {gold} gold.")
    for message in add_xp(player, monster.xp_reward):
        good(message)
    if dropped_item:
        player["inventory"].append(dropped_item)
        info(f"The monster dropped: {dropped_item}")

    if final_boss:
        player["inventory"].append("Crown of Dawn")
        complete_boss_quest(player)
        return "boss_defeated"

    record_monster_victory(player, monster.name)
    if dropped_item == "Herb":
        player["herbs_collected"] += 1
        # Quest check runs after the herb count has been updated.
        from quest import check_side_quests
        check_side_quests(player)
    return "victory"
