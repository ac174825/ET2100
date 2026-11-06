MAPS = {
    "Eldoria Village": [
        "##########",
        "#........#",
        "#.##..#..#",
        "#........#",
        "#..##....#",
        "#........#",
        "##########"
    ],
    "Whispering Woods": [
        "############",
        "#....#.....#",
        "#....#.....#",
        "#.##...##..#",
        "#..........#",
        "###.####...#",
        "#..........#",
        "############"
    ],
    "Shadow Fortress": [
        "##############",
        "#....#.......#",
        "#....#..##...#",
        "#........#...#",
        "###.##...#...#",
        "#...........#",
        "#.######....#",
        "#...........#",
        "##############"
    ]
}

def draw_map(map_name, position):
    print(f"\n--- {map_name} ---")
    print("@ = You | # = Wall | . = Walkable")
    px, py = position
    for y, row in enumerate(MAPS[map_name]):
        print("".join("@" if (x, y) == (px, py) else tile
                     for x, tile in enumerate(row)))

def is_walkable(map_name, x, y):
    layout = MAPS[map_name]
    return 0 <= y < len(layout) and 0 <= x < len(layout[y]) and layout[y][x] != "#"

def starting_position(map_name):
    return [1, 1]

def move_player(player, direction):
    moves = {"w": (0, -1), "s": (0, 1), "a": (-1, 0), "d": (1, 0)}
    if direction not in moves:
        return False, "Use W, A, S, or D."
    x, y = player["position"]
    dx, dy = moves[direction]
    nx, ny = x + dx, y + dy
    if not is_walkable(player["current_map"], nx, ny):
        return False, "A wall blocks your way."
    player["position"] = [nx, ny]
    return True, "You moved."
