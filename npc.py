from quest import complete_elder_step, check_side_quests
from utils import ask, info, good, warn

NPCS = {
    "Eldoria Village": [
        {
            "name": "Elder Mira",
            "dialogue": "The Crystal of Dawn was broken into three relics. Find them, then face the Shadow King.",
            "role": "elder"
        },
        {
            "name": "Tomas the Smith",
            "dialogue": "A sharp blade helps, but a prepared adventurer carries potions and learns new skills.",
            "role": "smith"
        },
        {
            "name": "Lina the Healer",
            "dialogue": "Please bring me two Herbs from the woods. I can reward you for helping the sick.",
            "role": "herbalist"
        }
    ],
    "Whispering Woods": [
        {
            "name": "Ranger Rowan",
            "dialogue": "Two wolves have been stalking the forest trail. Defeat them and the path will be safer.",
            "role": "ranger"
        },
        {
            "name": "Witch Elowen",
            "dialogue": "Magic rewards patience. Fireball burns foes, while Heal restores your strength.",
            "role": "witch"
        }
    ],
    "Shadow Fortress": [
        {
            "name": "Prisoner Kael",
            "dialogue": "The relics weaken the king's shadow armor. You have a chance now—do not waste it.",
            "role": "prisoner"
        }
    ]
}

def talk_to_npc(player):
    people = NPCS.get(player["current_map"], [])
    if not people:
        info("There is nobody here to talk to.")
        return
    print("\nPeople nearby:")
    for index, person in enumerate(people, 1):
        print(f"{index}. {person['name']}")
    print("0. Leave")
    choice = ask("Who would you like to talk to? ")
    if choice == "0":
        return
    if not choice.isdigit() or not 1 <= int(choice) <= len(people):
        warn("Please select a valid NPC number.")
        return

    person = people[int(choice) - 1]
    print(f"\n{person['name']}: \"{person['dialogue']}\"")
    if person["role"] == "elder":
        complete_elder_step(player)
    elif person["role"] == "herbalist":
        if player["herbs_collected"] >= 2:
            check_side_quests(player)
        else:
            info(f"Lina still needs {2 - player['herbs_collected']} Herb(s).")
    elif person["role"] == "ranger":
        info(f"Rowan needs you to defeat {max(0, 2 - player['wolves_defeated'])} more Wolf/Wolves.")
