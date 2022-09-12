import sys
import time

from check import check_start_choice,\
    check_actions_choice,\
    check_monster_hp,\
    check_hero_hp

from service import defeated_monster

from hero_classes import Hero


def start_game():
    """
    Функция начала игры

    Returns:
        Ввод пользователя
    """

    print(f'Добро пожаловать в игру, чтобы начать нажмите 1\n'
          f'для того чтобы выйти нажмите 2')
    user_input = 4
    while not check_start_choice(user_input):
        user_input = int(input())
        if user_input:
            return user_input
        else:
            print('Неверный ввод,пожалуйста введите значение 1 или 2')


def show_hero(hero_list: list):
    """
    Функция проверяет живы ли все герои, если да, то печатает их статы
    Далее печатается выбор героев

    Args:
        hero_list: список героев

    Returns:
        Выбранного героя
    """
    for hero in hero_list:
        time.sleep(0.1)
        if check_hero_hp(hero):
            sys.exit(f"Герой {hero.name} побеждён,попробуйте снова")
        else:
            print(
                f'{hero.name} имеет {hero.current_hp} хп, и {hero.current_mana} маны\n'
                f'может нанести {hero.damage} от руки\n\n'
            )

    count = 0
    for hero in hero_list:
        time.sleep(0.1)
        count += 1
        print(f'Выберите кем играть: {hero.name}- {count}\n')
    user_input = 6
    while not check_actions_choice(user_input, len(hero_list)):
        user_input = int(input())
    return hero_list[user_input - 1]


def show_monster(monster_list: list, hero_list: list):
    """
    Функция проверяет живы ли все монстры, если да, то они печатаются
    Далее печатается выбор монстра для атаки

    Args:
        monster_list: список монстров
        hero_list: список героев

    Returns:
        Выбранного монстра
    """
    for monster in monster_list:
        time.sleep(0.1)
        if check_monster_hp(monster):
            print(
                f'{monster.name} имеет {monster.current_hp} хп\n'
                f'И может нанести {monster.damage} от руки\n\n'
            )
        else:
            print(f"Побеждён {monster.name},всем герои получают 10 маны")
            defeated_monster(hero_list)
            monster_list.remove(monster)

    count = 0
    for monster in monster_list:
        time.sleep(0.1)
        count += 1
        print(f'Выберите кого атаковать: {monster.name}- {count}\n')

    user_input = 6
    while not check_actions_choice(user_input, len(monster_list)):
        user_input = int(input())
    return monster_list[user_input - 1]


def block_hero(hero: Hero):
    """
    Функция печатает какой герой заблокирован

    Args:
        hero: Героя

    """
    print(f'Герой {hero.name} заблокирован для этого раунда')


def damage_or_ability():
    """
    Функция выбора действия

    Returns:
        Ввод пользователя
    """

    user_input = 4
    while not check_start_choice(user_input):
        user_input = int(input('Для того чтобы атаковать нажмите 1\n'
                               'Для того чтобы применить способность нажмите 2\n'))
        if check_start_choice(user_input):
            return user_input
        else:
            print("Неверный ввод,повторите попытку")
            