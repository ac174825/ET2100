from item import ITEMS, describe_item
from utils import ask, good, warn, info

def show_inventory(player):
    print("\n========== INVENTORY ==========")
    if not player["inventory"]:
        print("Your inventory is empty.")
    else:
        counts = {}
        for item in player["inventory"]:
            counts[item] = counts.get(item, 0) + 1
        for name, quantity in counts.items():
            print(f"{name} x{quantity} — {describe_item(name)}")
    print("===============================\n")

def use_item(player):
    usable = [
        name for name in player["inventory"]
        if name in ITEMS and ITEMS[name]["type"] == "healing"
    ]
    if not usable:
        warn("You do not have any healing potions.")
        return
    print("\nHealing items:")
    for index, name in enumerate(usable, 1):
        print(f"{index}. {name} — {describe_item(name)}")
    print("0. Cancel")
    choice = ask("Which item do you want to use? ")
    if choice == "0":
        return
    if not choice.isdigit() or not 1 <= int(choice) <= len(usable):
        warn("Invalid item selection.")
        return
    item_name = usable[int(choice) - 1]
    amount = ITEMS[item_name]["power"]
    old_hp = player["hp"]
    player["hp"] = min(player["max_hp"], player["hp"] + amount)
    if player["hp"] == old_hp:
        info("Your HP is already full. The potion was not used.")
        return
    player["inventory"].remove(item_name)
    good(f"{item_name} restored {player['hp'] - old_hp} HP.")
