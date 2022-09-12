from monster_classes import Monster
from hero_classes import Hero


def check_start_choice(inp: int) -> bool:
    """
    Проверка корректности выбора пользователя
    Args:
        inp: ввод пользователя
    Returns:
        Статус проверки
    """
    if 0 < int(inp) < 3:
        return True
    return False


def check_hero_choice(inp: int) -> bool:
    """
    Проверка корректности выбора пользователя
    Args:
        inp: ввод пользователя
    Returns:
        Статус проверки
    """
    if 1 <= int(inp) <= 3:
        return True
    return False


def check_list_of_hero(hero_list: list) -> bool:
    """
    Проверка пустоты списка
    Args:
        hero_list: список героев
    Returns:
        Статус проверки
    """
    if hero_list == []:
        return True
    return False


def check_actions_choice(inp: int, len_of_list: int) -> bool:
    """
    Проверка корректности выбора пользователя
    Args:
        inp: ввод пользователя
        len_of_list: длинна списка
    Returns:
        Статус проверки
    """
    if len_of_list >= inp:
        return True
    return False


def check_monster_hp(monster: Monster) -> bool:
    """
    Проверка жив ли монстр
    Args:
        monster: текущий монстр
    Returns:
        Статус проверки
    """
    if monster.current_hp > 0:
        return True
    return False


def check_hero_mana(hero: Hero) -> bool:
    """
    Проверяет можно ли добавить маны герою
    Args:
        hero: текущий герой
    Returns:
        Статус проверки
    """
    if hero.current_mana >= hero.max_mana:
        return True
    return False


def check_hero_hp(hero) -> bool:
    """
    Проверка жив ли герой
    Args:
        hero: текущий монстр
    Returns:
        Статус проверки
    """
    if hero.current_hp <= 0:
        return True
    return False
