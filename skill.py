class Skill:
    name = "Skill"
    cooldown = 0
    description = "A special action."

    def use(self, player, monster=None):
        return "Nothing happens."

class Strike(Skill):
    name = "Strike"
    cooldown = 0
    description = "A dependable attack."

    def use(self, player, monster=None):
        damage = player["attack"]
        if monster:
            monster.take_damage(damage)
        return f"You strike for {damage} damage."

class Fireball(Skill):
    name = "Fireball"
    cooldown = 2
    description = "Deal twice your normal attack damage."

    def use(self, player, monster=None):
        damage = player["attack"] * 2
        if monster:
            monster.take_damage(damage)
        return f"Fireball deals {damage} damage."

class Heal(Skill):
    name = "Heal"
    cooldown = 3
    description = "Restore up to 35 HP."

    def use(self, player, monster=None):
        restored = min(35, player["max_hp"] - player["hp"])
        player["hp"] += restored
        return f"You restored {restored} HP."

class PowerSlash(Skill):
    name = "Power Slash"
    cooldown = 2
    description = "Deal three times your normal attack damage."

    def use(self, player, monster=None):
        damage = player["attack"] * 3
        if monster:
            monster.take_damage(damage)
        return f"Power Slash deals {damage} damage."

SKILL_TYPES = {
    "Strike": Strike,
    "Fireball": Fireball,
    "Heal": Heal,
    "Power Slash": PowerSlash
}

SKILL_PRICES = {"Fireball": 35, "Heal": 30, "Power Slash": 50}

def create_skill(skill_name):
    return SKILL_TYPES[skill_name]()

def learn_skill(player, skill_name):
    if skill_name not in SKILL_TYPES:
        return False, "That skill is not available."
    if skill_name in player["skills"]:
        return False, "You already know that skill."
    price = SKILL_PRICES.get(skill_name, 0)
    if player["gold"] < price:
        return False, f"You need {price} gold."
    player["gold"] -= price
    player["skills"].append(skill_name)
    player["cooldowns"][skill_name] = 0
    return True, f"You learned {skill_name}!"
