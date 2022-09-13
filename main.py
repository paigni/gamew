import time
from check import check_list_of_hero

from service import list_of_heroes, \
    amount_monsters, \
    list_of_monsters,\
    block_hero,\
    defeated_monster

from interface import show_hero, \
    damage_or_ability, \
    show_monster,\
    choice_hero,\
    choice_monster



def main():
    copy_list_heroes = list_of_heroes.copy()
    monsters = list_of_monsters[:amount_monsters]

    while True:

        if not check_list_of_hero(copy_list_heroes):
            show_hero(copy_list_heroes)
            hero = choice_hero(copy_list_heroes)
            hero.ability()
            hero_choice = damage_or_ability()
            show_monster(monsters)

            if hero_choice == 1:
                hero.hero_damage(choice_monster(monsters))
            elif hero_choice == 2:
                if hero.name == "Paladin":
                    hero.holy_land(monsters)
                elif hero.name == "Mage":
                    hero.fire_ball(choice_monster(monsters))
                elif hero.name == "Priest":
                    hero.healing_light(list_of_heroes)

            monsters = defeated_monster(list_of_heroes, monsters)

            block_hero(hero, copy_list_heroes)

        else:
            for monster in monsters:
                monster.monster_damage(list_of_heroes)
                time.sleep(3)
            copy_list_heroes = list_of_heroes.copy()


if __name__ == '__main__':
    main()
