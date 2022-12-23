class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0

class Cali(Enemy):
    def __init__(self):
        super().__init__(name="Cali: The Killer", hp=10, damage=2)

class UsTaskForce(Enemy):
    def __init__(self):
        super().__init__(name="US Task Force", hp=30, damage=4)

class Traitors(Enemy):
    def __init__(self):
        super().__init__(name="Traitors", hp=20, damage=3)

class ColumbianTaskForce(Enemy):
    def __init__(self):
        super().__init__(name="Columbian Task Force", hp=50, damage=10)

class LocalPolice(Enemy):
    def __init__(self):
        super().__init__(name="Local Police", hp=20, damage=6)

class OtherCountryEnemies(Enemy):
    def __init__(self):
        super().__init__(name="Other Country Police", hp=25, damage=2)