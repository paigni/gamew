def check_start_choice(inp):
    if 0 < int(inp) < 3:
        return True
    return False


def check_hero_choice(inp):
    if 1 <= int(inp) <= 3:
        return True
    return False


def check_list_of_hero(hero_list):
    if hero_list == []:
        return True
    return False


def check_monster_choice(inp, le_of_lis):
    if le_of_lis >= inp:
        return True
    return False


def check_hero_energy(mana):
    if mana >= 0:
        return True
    return False


def check_monster_hp(monst):
    if monst.current_hp > 0:
        return True
    return False
