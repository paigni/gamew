import random

from monster_classes import Rat, Goblin, Dragon, BigGoblin, DragonsBaby
from hero_classes import Mage, Paladin, Priest


rat = Rat()
goblin = Goblin()
dragon = Dragon()
big_goblin = BigGoblin()
dragons_baby = DragonsBaby()

list_of_monsters = [rat, goblin, dragon, big_goblin, dragons_baby]
amount_monsters = random.randint(1,4)



mage = Mage()
paladin = Paladin()
priest = Priest()
list_of_heroes = [mage, paladin, priest]


