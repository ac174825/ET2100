ITEMS = {
    "Small Potion": {
        "price": 12, "type": "healing", "power": 30,
        "description": "Restores up to 30 HP."
    },
    "Large Potion": {
        "price": 25, "type": "healing", "power": 70,
        "description": "Restores up to 70 HP."
    },
    "Herb": {
        "price": 8, "type": "quest", "power": 0,
        "description": "A medicinal herb wanted by Lina."
    },
    "Wolf Fang": {
        "price": 5, "type": "loot", "power": 0,
        "description": "A trophy taken from a wolf."
    },
    "Mana Crystal": {
        "price": 15, "type": "loot", "power": 0,
        "description": "A crystal humming with magic."
    },
    "Troll Hide": {
        "price": 10, "type": "loot", "power": 0,
        "description": "A tough piece of monster hide."
    },
    "Crown of Dawn": {
        "price": 0, "type": "quest", "power": 0,
        "description": "Proof that the Shadow King has fallen."
    }
}

def describe_item(name):
    item = ITEMS.get(name)
    if item:
        return item["description"]
    return "An unusual item."
