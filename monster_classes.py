class Monster:
    name = 'name'
    hp = 0
    damage = 0

    def

class Rat(Monster):
    name = 'rat'
    hp = 10
    damage = 3


class Goblin(Monster):
    name = 'goblin'
    hp = 18
    damage = 7


class Dragon(Monster):
    name = 'dragon'
    hp = 50
    damage = 15


class BigGoblin(Monster):
    name = 'big_goblin'
    hp = 25
    damage = 10


class DragonsBaby(Monster):
    name = 'dragons_baby'
    hp = 37
    damage = 8



rat = Rat()
goblin = Goblin()
dragon = Dragon()
big_goblin = BigGoblin()
dragons_baby = DragonsBaby()

list_of_monsters = [rat, goblin, dragon, big_goblin, dragons_baby]
