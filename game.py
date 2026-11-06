import random
from auth import account_screen
from database import get_progress, save_progress
from player import create_player, show_character
from game_map import MAPS, draw_map, move_player, starting_position
from npc import talk_to_npc
from shop import visit_shop
from inventory import show_inventory, use_item
from quest import show_quests
from combat import battle
from utils import ask, heading, good, warn, info

def save_game(username, player):
    save_progress(username, player)

def travel(player):
    destinations = list(MAPS.keys())
    print("\nTravel destinations:")
    for number, destination in enumerate(destinations, 1):
        print(f"{number}. {destination}")
    print("0. Cancel")
    choice = ask("Where do you want to travel? ")
    if choice == "0":
        return
    if not choice.isdigit() or not 1 <= int(choice) <= len(destinations):
        warn("Invalid destination.")
        return
    destination = destinations[int(choice) - 1]
    if destination == "Shadow Fortress" and player["main_quest_stage"] < 2:
        warn("The fortress gate is sealed. Recover all three relics first.")
        return
    player["current_map"] = destination
    player["position"] = starting_position(destination)
    good(f"You traveled to {destination}.")

def explore(player):
    draw_map(player["current_map"], player["position"])
    direction = ask("Move W/A/S/D, or press Enter to stop: ").lower()
    if direction == "":
        return
    moved, message = move_player(player, direction)
    (info if moved else warn)(message)
    if moved and player["current_map"] != "Eldoria Village" and random.random() < 0.35:
        battle(player)

def run_game(username):
    saved = get_progress(username)
    if saved:
        player = saved
        good(f"Welcome back, {player['name']}! Your saved game has loaded.")
    else:
        name = ask("What is your character's name? ")
        player = create_player(name)
        save_game(username, player)
        good(f"Welcome to Eldoria, {player['name']}!")

    while True:
        if player["boss_defeated"]:
            heading("ELDORIA HAS BEEN SAVED!")
            good("You defeated the Shadow King and restored the Crystal of Dawn.")
            print("Your completed adventure remains saved. You can explore or quit.")
        print(f"\n{player['name']} | Lv {player['level']} | "
              f"HP {player['hp']}/{player['max_hp']} | Gold {player['gold']}")
        print(f"Location: {player['current_map']}")
        print("\n1. Explore / move")
        print("2. Talk to an NPC")
        print("3. Character progress")
        print("4. Quest journal")
        print("5. Inventory")
        print("6. Use a healing item")
        print("7. Visit shop")
        print("8. Travel")
        print("9. Fight a monster")
        print("10. Challenge the Final Boss")
        print("11. Save game")
        print("0. Save and quit")
        choice = ask("Choose an action: ")

        if choice == "1":
            explore(player)
        elif choice == "2":
            talk_to_npc(player)
        elif choice == "3":
            show_character(player)
        elif choice == "4":
            show_quests(player)
        elif choice == "5":
            show_inventory(player)
        elif choice == "6":
            use_item(player)
        elif choice == "7":
            visit_shop(player)
        elif choice == "8":
            travel(player)
        elif choice == "9":
            if player["current_map"] == "Eldoria Village":
                warn("The village is safe. Travel to the woods to find monsters.")
            elif player["current_map"] == "Shadow Fortress" and player["main_quest_stage"] < 2:
                warn("The fortress is too dangerous before you recover the relics.")
            else:
                battle(player)
        elif choice == "10":
            if player["current_map"] != "Shadow Fortress":
                warn("Travel to the Shadow Fortress first.")
            elif player["main_quest_stage"] < 2 or len(player["relics"]) < 3:
                warn("You need all three relics before challenging the Shadow King.")
            elif player["boss_defeated"]:
                info("The Shadow King has already been defeated.")
            else:
                battle(player, final_boss=True)
        elif choice == "11":
            save_game(username, player)
            good("Game saved.")
        elif choice == "0":
            save_game(username, player)
            good("Progress saved. Thank you for playing!")
            break
        else:
            warn("Invalid choice. Enter a number from 0 to 11.")

        # Save after each menu action, including battles, travel, and purchases.
        save_game(username, player)

def start():
    username = account_screen()
    if username is None:
        print("Thanks for playing!")
        return
    run_game(username)
