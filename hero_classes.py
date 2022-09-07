import random


class Hero:
    name = 'name'
    max_hp = 0
    current_hp = max_hp
    max_mana = 0
    current_mana = max_mana
    damage = 0
    min_damage = 0
    max_damage = 0


    def hero_damage(self):
        damage = random.randint(self.min_damage, self.max_damage)
        return damage


class Mage(Hero):
    name = 'Mage'
    max_hp = 45
    current_hp = max_hp
    max_mana = 50
    current_mana = max_mana
    damage = 7
    min_damage = 10
    max_damage = 25


    def fire_ball(self):
        damage = Hero.hero_damage(self)
        self.current_mana -= 10
        return damage


class Paladin(Hero):
    name = 'Paladin'
    max_hp = 70
    current_hp = max_hp
    max_mana = 30
    current_mana = max_mana
    damage = 12
    min_damage = 8
    max_damage = 12


    def holy_land(self, list_of_monst):
        self.current_mana -= 8
        for monster in list_of_monst:
            damage = Hero.hero_damage(self)
            monster_hp = monster.hp - damage
        return list_of_monst


class Priest(Hero):
    name = 'Paladin'
    max_hp = 50
    current_hp = max_hp
    max_mana = 120
    current_mana = max_mana
    damage = 5

    def healing_light(self,list_of_hero):
        for hero in list_of_hero:
            hero.current_hp += 20
            print(hero.current_hp)


mage = Mage()
paladin = Paladin()
priest = Priest()






list_of_heroes = [mage,paladin,priest]

priest.healing_light(list_of_heroes)



