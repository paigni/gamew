import random


class Monster:
    name = 'name'
    max_hp = 0
    current_hp = max_hp
    damage = 0

    def monster_damage(self, list_of_hero):
        len_list = len(list_of_hero)
        random_index = random.randrange(len_list)
        hero = list_of_hero[random_index]
        print(f'Герою {hero.name} нанесено {self.damage} урона')
        hero.current_hp -= self.damage


class Rat(Monster):
    name = 'rat'
    max_hp = 10
    current_hp = max_hp
    damage = 3


class Goblin(Monster):
    name = 'goblin'
    max_hp = 18
    current_hp = max_hp
    damage = 7


class Dragon(Monster):
    name = 'dragon'
    max_hp = 50
    current_hp = max_hp
    damage = 15


class BigGoblin(Monster):
    name = 'big_goblin'
    max_hp = 25
    current_hp = max_hp
    damage = 10


class DragonsBaby(Monster):
    name = 'dragons_baby'
    max_hp = 37
    current_hp = max_hp
    damage = 8
