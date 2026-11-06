from item import ITEMS
from skill import SKILL_PRICES, learn_skill
from utils import ask, good, warn

SHOP_ITEMS = ["Small Potion", "Large Potion", "Herb"]

def visit_shop(player):
    if player["current_map"] != "Eldoria Village":
        warn("The shop is located in Eldoria Village.")
        return
    while True:
        print("\n========== TOMAS'S SHOP ==========")
        for index, name in enumerate(SHOP_ITEMS, 1):
            print(f"{index}. {name} — {ITEMS[name]['price']} gold")
        print("\nLearnable skills:")
        for name, price in SKILL_PRICES.items():
            print(f"{name} — {price} gold")
        print("0. Leave shop")
        choice = ask("Type an item/skill name to buy, or 0 to leave: ")
        if choice == "0":
            return
        if choice in SHOP_ITEMS:
            price = ITEMS[choice]["price"]
            if player["gold"] < price:
                warn("You do not have enough gold.")
            else:
                player["gold"] -= price
                player["inventory"].append(choice)
                good(f"You bought {choice}.")
        elif choice in SKILL_PRICES:
            success, message = learn_skill(player, choice)
            (good if success else warn)(message)
        else:
            warn("That item or skill is not sold here.")
