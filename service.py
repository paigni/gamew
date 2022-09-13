import random

from monster_classes import Rat, Goblin, Dragon, BigGoblin, DragonsBaby
from hero_classes import Mage, Paladin, Priest, Hero
from check import check_hero_mana, check_monster_hp

RAT = Rat()
GOBLIN = Goblin()
DRAGON = Dragon()
BIG_GOBLIN = BigGoblin()
DRAGON_BABY = DragonsBaby()

list_of_monsters = [RAT, GOBLIN, DRAGON, BIG_GOBLIN, DRAGON_BABY]
amount_monsters = random.randint(2, 5)

MAGE = Mage()
PALADIN = Paladin()
PRIEST = Priest()
list_of_heroes = [MAGE, PALADIN, PRIEST]


def defeated_monster(hero_list, monster_list:list):
    """
    Когда умер один из монстров-
    Функция добавляет 10 маны всем героям, если их мана не больше максимальной


    Args:
        monster_list: список монстров
        hero_list: список героев

    Returns:
    """
    for monster in monster_list:
        if not check_monster_hp(monster):
            monster_list.remove(monster)
            for hero in hero_list:
                hero.current_mana += 10
                if check_hero_mana(hero):
                    hero.current_mana = hero.max_mana
            print(f"Побеждён {monster.name},всем герои получают 10 маны")
    return monster_list


def block_hero(hero: Hero, copy_list_heroes: list):
    """
    Функция печатает какой герой заблокирован

    Args:
        hero: Героя
        copy_list_heroes: cписок героев

    """
    copy_list_heroes.remove(hero)
    print(f'Герой {hero.name} заблокирован для этого раунда')


