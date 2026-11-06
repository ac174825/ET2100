# The Shattered Kingdom — Terminal RPG

## Install with uv
Open a terminal in this folder and run:

```bash
uv add colorama
uv add tinydb
```

If you are not using uv, you can install with:
`python -m pip install colorama tinydb`

## Run
```bash
uv run python main.py
```
Or:
`python main.py`

## Saving
Register an account, then log in. TinyDB creates `game_data.json` in this folder.
The game automatically saves after each menu action and when you choose Save and Quit.
Log in with the same account later to continue.

Saved data includes the username/account, level, XP, HP, gold, inventory, learned skills,
skill cooldowns, current map, map position, main quest stage, side quest progress,
monster defeats, and final-boss status.

## Controls
- Use the numbered menu.
- On maps, use W/A/S/D to move.
- `#` represents a wall. `@` is your character.
- Monsters appear when exploring dangerous maps and can also be challenged from the menu.
- Talk to NPCs, visit the shop in Eldoria Village, and check the quest journal.

## Python files
- `main.py`: starts the program
- `game.py`: main game loop and menus
- `auth.py`: registration and login
- `database.py`: TinyDB account and save operations
- `player.py`: player data and leveling
- `monster.py`: Monster parent class and five subclasses
- `skill.py`: Skill parent class and skill subclasses
- `combat.py`: turn-based battles and rewards
- `item.py`: item definitions
- `inventory.py`: inventory display and item use
- `quest.py`: main quest and side quests
- `npc.py`: five NPCs and their dialogue
- `shop.py`: item and skill purchases
- `game_map.py`: maps, movement, and collision
- `utils.py`: terminal colors and input validation
