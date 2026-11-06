import random

class Monster:
    name = "Monster"
    max_hp = 20
    attack = 5
    xp_reward = 10
    gold_min = 2
    gold_max = 8
    possible_drops = ["Small Potion"]

    def __init__(self):
        self.hp = self.max_hp

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp = max(0, self.hp - max(0, damage))

    def loot(self):
        gold = random.randint(self.gold_min, self.gold_max)
        item = random.choice(self.possible_drops + [None, None])
        return gold, item

class Goblin(Monster):
    name = "Goblin"
    max_hp = 28
    attack = 7
    xp_reward = 15
    gold_min, gold_max = 4, 12
    possible_drops = ["Small Potion", "Herb"]

class Wolf(Monster):
    name = "Wolf"
    max_hp = 35
    attack = 9
    xp_reward = 20
    gold_min, gold_max = 5, 14
    possible_drops = ["Wolf Fang", "Small Potion"]

class Skeleton(Monster):
    name = "Skeleton"
    max_hp = 43
    attack = 10
    xp_reward = 24
    gold_min, gold_max = 7, 16
    possible_drops = ["Mana Crystal", "Small Potion"]

class Troll(Monster):
    name = "Troll"
    max_hp = 65
    attack = 13
    xp_reward = 35
    gold_min, gold_max = 10, 22
    possible_drops = ["Troll Hide", "Large Potion"]

class ShadowKing(Monster):
    name = "Shadow King"
    max_hp = 160
    attack = 18
    xp_reward = 120
    gold_min, gold_max = 60, 100
    possible_drops = ["Crown of Dawn"]

def create_random_monster(map_name):
    if map_name == "Whispering Woods":
        monster_class = random.choice([Goblin, Wolf, Skeleton, Troll])
    else:
        monster_class = random.choice([Skeleton, Troll])
    return monster_class()
