class Battle():
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def Hit(self, enemy):
        print(f"{self.name} hit {enemy.name}")
        self.DamageHit(enemy)

    def DamageHit(self, enemy):
        damage = int(self.power / 10)
        enemy.health -= damage
        print(f"Hit damage: {damage}")
        print(f"{enemy.name} health: {enemy.health} / 100")

    def Kick(self, enemy):
        print(f"{self.name} kicked {enemy.name}")
        self.DamageKick(enemy)

    def DamageKick(self, enemy):
        damage = int(self.power / 7)
        enemy.health -= damage
        print(f"Kick damage: {damage}")
        print(f"{enemy.name} health: {enemy.health} / 100")

    @staticmethod
    def print_health(fighter):
        print(f"{fighter.name} health: {fighter.health} / 100")

fighter_1 = Battle("Asep", 100, 20)
fighter_2 = Battle("Udin", 100, 25)

i = 0
while True:
    i += 1
    print("\nRound", i)
    fighter = int(input("Choose Fighter:\n1) Fighter 1 (Hit)\n2) Fighter 1 (Kick)\n3) Fighter 2 (Hit)\n4) Fighter 2 (Kick)\nChoice (1 | 2 | 3 | 4): "))
    
    if fighter == 1:
        fighter_1.Hit(fighter_2)
    elif fighter == 2:
        fighter_1.Kick(fighter_2)
    elif fighter == 3:
        fighter_2.Hit(fighter_1)
    elif fighter == 4:
        fighter_2.Kick(fighter_1)

    if i >= 5:
        status = input("Continue (Y/N): ").upper()
        if status != "Y":
            break

print("-"*5, "End", "-"*5)
fighter_1.print_health(fighter_1)
fighter_2.print_health(fighter_2)