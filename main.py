import time
from check import check_list_of_hero
from service import list_of_heroes, \
    amount_monsters, \
    list_of_monsters
from interface import show_hero, damage_or_ability, show_monster, block_hero


def main():
    copy_list_heroes = list_of_heroes.copy()
    monsters = list_of_monsters[:amount_monsters]

    while True:
        if not check_list_of_hero(copy_list_heroes):
            hero = show_hero(copy_list_heroes)
            hero_choice = damage_or_ability()
            if hero_choice == 1:
                hero.hero_damage(show_monster(monsters, list_of_heroes))
            elif hero_choice == 2:
                hero.ability()
                if hero.name == "Paladin":
                    hero.holy_land(monsters)
                elif hero.name == "Mage":
                    hero.fire_ball(show_monster(monsters, list_of_heroes))
                elif hero.name == "Priest":
                    hero.healing_light(list_of_heroes)
            copy_list_heroes.remove(hero)
            block_hero(hero)

        else:
            for monster in monsters:
                monster.monster_damage(list_of_heroes)
                time.sleep(3)
            copy_list_heroes = list_of_heroes.copy()


if __name__ == '__main__':
    main()
