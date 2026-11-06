from player import add_xp
from utils import good, info

MAIN_QUEST_STEPS = [
    "Speak with Elder Mira in Eldoria Village.",
    "Win three battles in the Whispering Woods to recover the Ember, Tide, and Root Relics.",
    "Travel to the Shadow Fortress and defeat the Shadow King."
]

def show_quests(player):
    stage = player["main_quest_stage"]
    print("\n========== QUEST JOURNAL ==========")
    if player["boss_defeated"]:
        print("MAIN QUEST: COMPLETE — The Shadow King has been defeated!")
    else:
        print(f"MAIN QUEST — The Shattered Kingdom (Step {stage + 1}/3)")
        print(MAIN_QUEST_STEPS[stage])
        if stage == 1:
            print(f"Relics recovered: {len(player['relics'])}/3")
    print("\nSIDE QUEST 1 — Herbal Remedy")
    print("Collect 2 Herbs for Lina. Reward: 25 gold and 25 XP.")
    print("Status:", "Complete" if player["herb_quest_complete"] else f"{player['herbs_collected']}/2 Herbs")
    print("\nSIDE QUEST 2 — Wolf Problem")
    print("Defeat 2 Wolves for Ranger Rowan. Reward: 30 gold and 30 XP.")
    print("Status:", "Complete" if player["wolf_quest_complete"] else f"{player['wolves_defeated']}/2 Wolves")
    print("===================================\n")

def complete_elder_step(player):
    if player["main_quest_stage"] == 0:
        player["main_quest_stage"] = 1
        good("Main quest updated: recover three relics from the Whispering Woods!")

def record_monster_victory(player, monster_name):
    if monster_name == "Wolf":
        player["wolves_defeated"] += 1

    if player["main_quest_stage"] == 1 and player["current_map"] == "Whispering Woods":
        relics = ["Ember Relic", "Tide Relic", "Root Relic"]
        if len(player["relics"]) < 3:
            relic = relics[len(player["relics"])]
            player["relics"].append(relic)
            good(f"You recovered the {relic}!")
        if len(player["relics"]) == 3:
            player["main_quest_stage"] = 2
            good("All three relics are restored. The Shadow Fortress is now accessible!")

    check_side_quests(player)

def check_side_quests(player):
    if player["herbs_collected"] >= 2 and not player["herb_quest_complete"]:
        player["herb_quest_complete"] = True
        player["gold"] += 25
        for message in add_xp(player, 25):
            good(message)
        good("Herbal Remedy complete! You received 25 gold and 25 XP.")

    if player["wolves_defeated"] >= 2 and not player["wolf_quest_complete"]:
        player["wolf_quest_complete"] = True
        player["gold"] += 30
        for message in add_xp(player, 30):
            good(message)
        good("Wolf Problem complete! You received 30 gold and 30 XP.")

def complete_boss_quest(player):
    player["boss_defeated"] = True
    good("MAIN QUEST COMPLETE! The Shadow King has been defeated. Eldoria is free!")
