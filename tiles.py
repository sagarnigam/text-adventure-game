import items, enemies, actions, world
 
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def intro_text(self):
        raise NotImplementedError()
 
    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves
 
    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
 
        return moves


class ColumbiaEntryPoint(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        You entered Columbia
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
 
    def add_loot(self, player):
        player.inventory.append(self.item)
 
    def modify_player(self, player):
        self.add_loot(player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
 
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()
 
class LocalPolice(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.LocalPolice())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant spider jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead spider rots on the ground.
            """

class OtherCountryEnemies(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.OtherCountryEnemies())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A wolf jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead wolf is on the ground.
             """

class ColumbianTaskForce(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.ColumbianTaskForce())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A wolf jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead wolf is on the ground.
             """

class Traitors(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Traitors())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A wolf jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead wolf is on the ground.
             """

class UsTaskForce(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.UsTaskForce())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A wolf jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead wolf is on the ground.
             """

class Cali(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Cali())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A wolf jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead wolf is on the ground.
             """

class GunPower(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.GunPower())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A wolf jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead wolf is on the ground.
             """

class MissilePower(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.MissilePower())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A wolf jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead wolf is on the ground.
             """

class MachineGun(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.MachineGun())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A wolf jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead wolf is on the ground.
             """

class GranadePower(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.GranadePower())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A wolf jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead wolf is on the ground.
             """

class ShotGumPower(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.ShotGumPower())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A wolf jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead wolf is on the ground.
             """

class AirStrikePower(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.AirStrikePower())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A wolf jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead wolf is on the ground.
             """


class LeaveColumbia(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
 
 
        Victory is yours!
        """
 
    def modify_player(self, player):
        player.victory = True