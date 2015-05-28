
class NotEnaughMana(Exception):
    pass

class NoMoreStartingPoints(Exception):
    pass

class Hero:

    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.health = health
        self.staring_health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.start_mana = mana
        self.min_health = 0
        self.min_mana = 0


    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        return self.health > self.min_health

    def can_cast(self):
        return self.mana > self.min_mana

    def take_damage(self,damage_points):
        if damage_points <= self.health:
            self.health -= damage_points
        elif damage_points > self.health:
            self.health = self.min_health

    def take_healing(self, healing_points):
        if self.get_health() > self.min_health:
            if (self.health + healing_points) > self.staring_health:
                self.health = self.staring_health
            else:
                self.health += healing_points
            return True
        return False

    # за довършване
    def take_mana(mana_points):

        if self.mana < self.start_mana and self.mana >= self.min_mana:
            self.mana += mana_points
            if self.mana >= self.start_mana:
                self.mana = self.start_mana

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

    def attack(self, by):

        if by == "weapon" and self.weapon != False:
            return self.weapon.damage

        if by == "spell" and self.spell != False:
            if self.spell.mana_cost <= self.get_mana():
                self.mana -= self.spell.mana_cost
                return self.spell.damage
            raise NotEnaughMana
        else:
            return 0

class Enemy(Hero):

    def __init__(self, _health, _mana, _damage):
        Hero.__init__(self, health=_health, mana=_mana, damage=_damage)

class Spell:

    def __init__(self, name, damage, mana_cost, cast_range):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range


class Weapon:

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Dungeon:

    OUR_HERO = "H"
    STARTING_POINT = "S"

    def __init__(self, load_dungeon):
        self.load_dungeon = load_dungeon

        with open(self.load_dungeon, "r") as f:
            self.map_data  = f.read()

    def print_map(self):
        return self.map_data

    def spawn(self, hero):
        if isinstance(hero , Hero):
             for elements in range(0, len(self.map_data)):
                if self.map_data[elements] == Dungeon.STARTING_POINT:
                    self.map_data = self.map_data.replace(self.map_data[elements], Dungeon.OUR_HERO)
                    return True
                elif hero.get_health() == 0  and Dungeon.STARTING_POINT in self.map_data:
                     self.map_data = self.map_data.replace(self.map_data[elements], Dungeon.OUR_HERO)
                     return True
                elif Dungeon.STARTING_POINT not in self.map_data:
                    raise NoMoreStartingPoints



"""
    def matrix_dungeon(self):
        for elements in self.data:
            if elements != '\n':
                self.rows_in_dungeon_list.append(elements)
            if elements == '\n':
                self.dungeon_list.append(self.rows_in_dungeon_list)
                self.rows_in_dungeon_list=[]
        print(self.dungeon_list)
        return self.dungeon_list
"""

"""
            self.rows_in_list_dungeon=[]
            print (rows)
            for element in rows:
                if element != '\n':
                   self.rows_in_list_dungeon.append(element)

            self.dungeon_list.append(self.rows_in_list_dungeon)
        return self.dungeon_list
"""










map = Dungeon("level1.txt")
h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
map.print_map()
map.spawn(h)
map.print_map()
map.spawn(h)
map.print_map()
map.spawn(h)

#print(map.matrix_dungeon())


