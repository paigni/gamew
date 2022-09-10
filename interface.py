from check import check_start_choice, check_monster_choice, check_list_of_hero,check_monster_hp
from service import list_of_heroes, amount_monsters, list_of_monsters


def start_game():
    print(f'Добро пожаловать в игру, чтобы начать нажмите 1\n'
          f'для того чтобы выйти нажмите 2')
    user_input = 4
    while not check_start_choice(user_input):
        user_input = int(input())
        if user_input:
            return user_input
        else:
            print('Неверный ввод,пожалуйста введите значение 1 или 2')


def show_hero(cop_list):
    """cop_list добавлен, для того чтобы блокировать героев"""
    for hero in cop_list:
        print(
            f'{hero.name} имеет {hero.current_hp} хп, и {hero.current_mana} маны\n'
            f'может нанести {hero.damage} от руки'
            f'\n'
        )

    count = 0
    for hero in cop_list:
        count += 1
        print(f'Выберите кем играть: {hero.name}- {count}\n')
    user_input = 6
    while not check_monster_choice(user_input, len(cop_list)):
        user_input = int(input())
        return cop_list[user_input-1]


def show_monster(monster_list):
    for monster in monster_list:
        if check_monster_hp(monster):
            print(
                f'{monster.name} имеет {monster.current_hp} хп\n'
                f'И может нанести {monster.damage} от руки'
                f'\n'
            )
        else:
            monster_list.remove(monster)

    count = 0
    for monster in monster_list:
        count += 1
        print(f'Выберите кого атаковать: {monster.name}- {count}\n')

    user_input = 6
    while not check_monster_choice(user_input, len(monster_list)):
        user_input = int(input())
        return monster_list[user_input - 1]


def mage_ability():
    print("Mage имеет способность огненный шар,которая бьёт \n"
          "по одному из монстров и наносит случайный урон от 10 до 25.")


def paladins_ability():
    print("Paladin имеет способность СВЯТАЯ ЗЕМЛЯ,которая бьёт \n"
          "по всем монстрам и наносит случайный урон от 8 до 12.")


def priest_ability():
    print("Priest имеет способность ИСЦЕЛЯЮЩИЙ СВЕТ,которая лечит \n"
          "всех героев на 20.")


def block_hero(hero_n):
    print(f'Герой {hero_n.name} заблокирован для этого раунда')


def damage_or_ability():
    user_input = 4
    while not check_start_choice(user_input):
        user_input = int(input('Для того чтобы атаковать нажмите 1\n'
                               'Для того чтобы применить способность нажмите 2\n'))
        if check_start_choice(user_input):
            return user_input


def game():
    copy_list_heroes = list_of_heroes.copy()
    monsters = list_of_monsters[:amount_monsters]
    while True:
        if not check_list_of_hero(copy_list_heroes):
            hero = show_hero(copy_list_heroes)
            if hero == list_of_heroes[0]:
                mage_ability()
                hero_choice = damage_or_ability()
                if hero_choice == 1:
                    hero.hero_damage(show_monster(monsters))
                    copy_list_heroes.remove(hero)
                elif hero_choice == 2:
                    hero.fire_ball(show_monster(monsters))
                    copy_list_heroes.remove(hero)
                block_hero(hero)
            elif hero == list_of_heroes[1]:
                paladins_ability()
                hero_choice = damage_or_ability()
                hero = list_of_heroes[1]
                if hero_choice == 1:
                    hero.hero_damage(show_monster(monsters))
                elif hero_choice == 2:
                    hero.holy_land(monsters)
                block_hero(hero)
                copy_list_heroes.remove(hero)
            elif hero == list_of_heroes[2]:
                priest_ability()
                hero_choice = damage_or_ability()
                hero = list_of_heroes[2]
                if hero_choice == 1:
                    hero.hero_damage(show_monster(monsters))
                elif hero_choice == 2:
                    hero.healing_light(list_of_heroes)
                block_hero(hero)
                copy_list_heroes.remove(hero)
                continue
        else:
            for monster in monsters:
                monster.monster_damage(list_of_heroes)
            copy_list_heroes = list_of_heroes.copy()




game()
