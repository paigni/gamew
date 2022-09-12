import random

from monster_classes import Rat, Goblin, Dragon, BigGoblin, DragonsBaby
from hero_classes import Mage, Paladin, Priest
from check import check_hero_mana

rat = Rat()
goblin = Goblin()
dragon = Dragon()
big_goblin = BigGoblin()
dragons_baby = DragonsBaby()

list_of_monsters = [rat, goblin, dragon, big_goblin, dragons_baby]
amount_monsters = random.randint(2, 5)

mage = Mage()
paladin = Paladin()
priest = Priest()
list_of_heroes = [mage, paladin, priest]


def defeated_monster(hero_list):
    """
    Функция добавляет 10 маны всем героям, если их мана не больше максимальной

    Args:
        hero_list: список героев

    Returns:
    """
    for hero in hero_list:
        hero.current_mana += 10
        if check_hero_mana(hero):
            hero.current_mana = hero.max_mana
