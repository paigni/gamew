from check import check_start_choice, check_hero_choice, check_monster_choice
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


def show_hero(list_of_hero, cop_list):
    """cop_list добавлен, для того чтобы блокировать героев"""
    for hero in list_of_hero:
        print(
            f'{hero.name} имеет {hero.current_hp} хп, и {hero.current_mana}\n'
            f'может нанести {hero.damage} от руки'
            f'\n'
        )

    count = 0
    for hero in cop_list:
        count += 1
        print(f'Выберите кем играть: {hero.name}- {count}\n')


def show_monster(monster_list):
    for monster in monster_list:
        print(
            f'{monster.name} имеет {monster.current_hp} хп\n'
            f'И может нанести {monster.damage} от руки'
            f'\n'
        )

    count = 0
    for monster in monster_list:
        count += 1
        print(f'Выберите кого атаковать: {monster.name}- {count}\n')

    user_input = 6
    while not check_monster_choice(user_input, len(monster_list)):
        user_input = int(input("Неверный ввод,повторите попытку"))
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


def damage_or_ability():
    user_input = int(input('Для того чтобы атаковать нажмите 1\n'
                           'Для того чтобы применить способность нажмите 2'))
    return user_input


def game():
    copy_list_heroes = list_of_heroes
    monsters = list_of_monsters[:amount_monsters]
    user_input = 4
    while not check_hero_choice(user_input):
        show_hero(list_of_heroes, copy_list_heroes)
        user_input = int(input())

        if check_hero_choice(user_input) and user_input == 1:
            mage_ability()
            if damage_or_ability() == 1:
                show_monster(monsters) - copy_list_heroes[0].damage

            elif damage_or_ability() == 2:
                show_monster(monsters) - copy_list_heroes[0].fire_ball()

        elif check_hero_choice(user_input) and user_input == 2:
            paladins_ability()
            if damage_or_ability() == 1:
                show_monster(monsters) - copy_list_heroes[1].damage

            elif damage_or_ability() == 2:
                copy_list_heroes[1].holy_land(monsters)

        elif check_hero_choice(user_input) and user_input == 3:
            if damage_or_ability() == 1:
                show_monster(monsters) - copy_list_heroes[2].damage

            elif damage_or_ability() == 2:
                copy_list_heroes[2].healing_light(list_of_heroes)


game()