import random
from monster_classes import Monster


class Hero:
    name = 'name'
    max_hp = 0
    current_hp = max_hp
    max_mana = 0
    current_mana = max_mana
    damage = 0
    min_damage = 0
    max_damage = 0

    def hero_damage(self, monst):
        monst.current_hp -= self.damage
        return monst.current_hp


class Mage(Hero):
    name = 'Mage'
    max_hp = 45
    current_hp = max_hp
    max_mana = 50
    current_mana = max_mana
    damage = 7
    min_damage = 10
    max_damage = 25

    def fire_ball(self, monster: Monster):
        """
        Метод наносит случайный урон выбранному монстру и отнимает 10 маны

        Args:
            monster: Выбранный монстр
        """
        damage = random.randint(self.min_damage, self.max_damage)
        self.current_mana -= 10
        monster.current_hp -= damage

    def ability(self):
        """
        Метод печатает способность героя
        """
        print(f"{self.name} имеет способность огненный шар,которая бьёт \n"
              "по одному из монстров и наносит случайный урон от 10 до 25.")


class Paladin(Hero):
    name = 'Paladin'
    max_hp = 70
    current_hp = max_hp
    max_mana = 30
    current_mana = max_mana
    damage = 12
    min_damage = 8
    max_damage = 12

    def holy_land(self, list_of_monster: list):
        """
        Метод наносит случайный урон всем монстрам и отнимает у героя 8 маны

        Args:
            list_of_monster: Список монстров
        """
        self.current_mana -= 8
        for monster in list_of_monster:
            damage = random.randint(self.min_damage, self.max_damage)
            monster.current_hp -= damage

    def ability(self):
        """
        Метод печатает способность героя
        """
        print(f"{self.name} имеет способность СВЯТАЯ ЗЕМЛЯ,которая бьёт \n"
              "по всем монстрам и наносит случайный урон от 8 до 12 и забирает 8 маны.")


class Priest(Hero):
    name = 'Priest'
    max_hp = 50
    current_hp = max_hp
    max_mana = 120
    current_mana = max_mana
    damage = 5

    def healing_light(self, list_of_hero: list):
        """
        Метод исцеляет всех героев на 20 единиц и забирает 10 маны

        Args:
            list_of_hero: Список героев
        """
        self.current_mana -= 10
        for hero in list_of_hero:
            hero.current_hp += 20

    def ability(self):
        """
        Метод печатает способность героя
        """
        print(f"{self.name} имеет способность ИСЦЕЛЯЮЩИЙ СВЕТ,которая лечит \n"  # переместить в классы героев
              "всех героев на 20 и забирает 10 маны.")
