# Base class for all items
class Item():
    # __init__ is the contructor method
    def __init__(self, name, description, value):
        self.name = name   # attribute of the Item class and any subclasses
        self.description = description # attribute of the Item class and any subclasses
        self.value = value # attribute of the Item class and any subclasses
    
    # __str__ method is used to print the object
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

# Extend the Items class
# Gold class will be a child or subclass of the superclass Item

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class GunPower(Weapon):
    def __init__(self):
        super().__init__(name="Gun Power",
                         description="M16 Gun obtained",
                         value=10,
                         damage=5)

class MissilePower(Weapon):
    def __init__(self):
        super().__init__(name="Missile Power",
                         description="Missile obtained",
                         value=20,
                         damage=10)

class MachineGun(Weapon):
    def __init__(self):
        super().__init__(name="Machine Gun",
                         description="Machine Gun obtained",
                         value=15,
                         damage=6)

class GranadePower(Weapon):
    def __init__(self):
        super().__init__(name="Granade Power",
                         description="GranadePower obtained",
                         value=10,
                         damage=4)

class ShotGumPower(Weapon):
    def __init__(self):
        super().__init__(name="Granade Power",
                         description="Shot gun Power obtained",
                         value=5,
                         damage=3)

class AirStrikePower(Weapon):
    def __init__(self):
        super().__init__(name="AirStrike Power",
                         description="AirStrike Power obtained",
                         value=5,
                         damage=3)