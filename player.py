from copy import deepcopy

DEFAULT_PLAYER = {
    "name": "Adventurer",
    "level": 1,
    "xp": 0,
    "hp": 100,
    "max_hp": 100,
    "attack": 10,
    "gold": 30,
    "inventory": ["Small Potion", "Small Potion"],
    "skills": ["Strike"],
    "cooldowns": {},
    "current_map": "Eldoria Village",
    "position": [1, 1],
    "main_quest_stage": 0,
    "relics": [],
    "herbs_collected": 0,
    "wolves_defeated": 0,
    "herb_quest_complete": False,
    "wolf_quest_complete": False,
    "boss_defeated": False,
    "total_monsters_defeated": 0
}

def create_player(name):
    player = deepcopy(DEFAULT_PLAYER)
    player["name"] = name.strip() or "Adventurer"
    return player

def add_xp(player, amount):
    player["xp"] += amount
    messages = []
    while player["xp"] >= player["level"] * 50:
        player["xp"] -= player["level"] * 50
        player["level"] += 1
        player["max_hp"] += 15
        player["attack"] += 3
        player["hp"] = player["max_hp"]
        messages.append(
            f"LEVEL UP! You are now level {player['level']}. "
            "Maximum HP and attack increased."
        )
    return messages

def show_character(player):
    print("\n========== CHARACTER ==========")
    print(f"Name: {player['name']}")
    print(f"Level: {player['level']} | XP: {player['xp']}/{player['level'] * 50}")
    print(f"HP: {player['hp']}/{player['max_hp']} | Attack: {player['attack']}")
    print(f"Gold: {player['gold']}")
    print(f"Map: {player['current_map']} | Position: {tuple(player['position'])}")
    print("Skills:", ", ".join(player["skills"]))
    print("Inventory:", ", ".join(player["inventory"]) if player["inventory"] else "Empty")
    print("Relics:", ", ".join(player["relics"]) if player["relics"] else "None")
    print(f"Monsters defeated: {player['total_monsters_defeated']}")
    print("================================\n")
