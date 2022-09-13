import sys
import time

from check import check_start_choice, \
    check_hero_hp, \
    check_user_input,\
    check_actions_choice


def start_game():
    """
    Функция начала игры

    Returns:
        Ввод пользователя
    """

    print(f'Добро пожаловать в игру, чтобы начать нажмите 1\n'
          f'для того чтобы выйти нажмите 2')
    user_input = 'd'
    while not check_user_input(user_input):
        user_input = int(input())
        if check_start_choice(user_input):
            return user_input
        else:
            print('Неверный ввод,пожалуйста введите значение 1 или 2')


def show_hero(hero_list: list):
    """
    Функция печатает статы героев
    Далее печатается выбор героев

    Args:
        hero_list: список героев
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


def show_monster(monster_list):
    """
    Функция проверяет живы ли все монстры, если да, то они печатаются
    Далее печатается выбор монстра для атаки
    """
    for monster in monster_list:
        time.sleep(0.1)
        print(
            f'{monster.name} имеет {monster.current_hp} хп\n'
            f'И может нанести {monster.damage} от руки\n\n'
        )


def choice_hero(hero_list):
    """
    Функция печатает не заблокированных героев, предлагая выбрать одного из

    Args:
        hero_list: список героев
    Returns:
        ввод пользователя
    """
    count = 0
    for hero in hero_list:
        time.sleep(0.1)
        count += 1
        print(f'Выберите кем играть: {hero.name}- {count}\n')
    user_input = 'd'
    while not check_user_input(user_input):
        user_input = input()
        if check_user_input(user_input):
            user_input = int(user_input)
            if check_actions_choice(user_input, len(hero_list)):
                break
        else:
            print("Неверный ввод,попробуйте снова")
    return hero_list[user_input - 1]



def choice_monster(monster_list):
    """
    Функция печатает живых монстров, предлагая выбрать одного из

    Args:
        monster_list: список героев
    Returns:
        ввод пользователя
    """
    count = 0
    for monster in monster_list:
        time.sleep(0.1)
        count += 1
        print(f'Выберите кого атаковать: {monster.name}- {count}\n')

    user_input = 'd'
    while not check_user_input(user_input):
        user_input = input()
        if check_user_input(user_input):
            user_input = int(user_input)
            if check_actions_choice(user_input, len(monster_list)):
                break
        else:
            print("Неверный ввод,попробуйте снова")
    return monster_list[user_input - 1]


def damage_or_ability():
    """
    Функция выбора действия

    Returns:
        Ввод пользователя
    """

    user_input = 'd'
    while not check_user_input(user_input):
        user_input = input('Для того чтобы атаковать нажмите 1\n'
                           'Для того чтобы применить способность нажмите 2\n')
        if check_user_input(user_input):
            user_input = int(user_input)
            if check_start_choice(user_input):
                return user_input
        else:
            print("Неверный ввод,повторите попытку")
