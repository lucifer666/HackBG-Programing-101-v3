from hero import Hero, Enemy, Weapon, Spell, NotEnaughMana
import unittest


class TestHero(unittest.TestCase):

    def setUp(self):
        self.h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        self.w = Weapon(name="The Axe of Destiny", damage=20)
        self.s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)

    def test_init(self):
        self.assertEqual(self.h.name, "Bron")
        self.assertEqual(self.h.title, "Dragonslayer")
        self.assertEqual(self.h.health, 100)
        self.assertEqual(self.h.mana, 100)
        self.assertEqual(self.h.mana_regeneration_rate, 2)
        self.assertEqual(self.h.start_mana, 100)
        self.assertEqual(self.h.damage, 0)

    def test_known_as(self):
        result = "Bron the Dragonslayer"
        self.assertEqual(self.h.known_as(), result)

    def test_is_alive(self):
        self.assertTrue(self.h.is_alive() is True)

    def test_take_damage(self):
        damage = self.h.take_damage(40)
        self.assertTrue(self.h.health is 60)

    def test_can_cast(self):
        self.assertTrue(self.h.can_cast() is True)

    def test_take_healing(self):
        self.h.take_damage(100)
        self.new_health = self.h.take_healing(30)
        self.assertTrue(self.h.health is 0)

    def test_take_mana(self):
        self.h.learn(self.s)
        self.h.attack(by="spell")
        self.h.take_mana(10)
        self.assertEqual(self.h.mana, 60)

    def test_attack(self):
        self.h.equip(self.w)
        self.assertEqual(self.h.attack(by="weapon"), 20)
        self.h.learn(self.s)
        self.assertEqual(self.h.attack(by="spell"), 30)

    def test_exception(self):
        self.h.learn(self.s)
        self.assertEqual(self.h.attack(by="spell"), 30)
        with self.assertRaises(NotEnaughMana):
            self.s.mana_cost = 50
            self.h.attack(by="spell")


class TestSpell(unittest.TestCase):

    def setUp(self):
        self.w = Weapon(name="The Axe of Destiny", damage=20)
        self.h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        self.s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)

    def test_init(self):
        self.assertEqual(self.s.name, "Fireball")
        self.assertEqual(self.s.damage, 30)
        self.assertEqual(self.s.mana_cost, 50)
        self.assertEqual(self.s.cast_range, 2)


class TestWeapon(unittest.TestCase):

    def setUp(self):
        self.w = Weapon(name="The Axe of Destiny", damage=20)
        self.h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

    def test_init(self):
        self.assertEqual(self.w.name, "The Axe of Destiny")
        self.assertEqual(self.w.damage, 20)


class TestEnemy(unittest.TestCase):

    def setUp(self):
        self.h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        self.enemy = Enemy(_health=100, _mana=100, _damage=20)

    def test_init(self):
        self.assertEqual(self.enemy.health, 100)
        self.assertEqual(self.enemy.mana, 100)
        self.assertEqual(self.enemy.damage, 20)


if __name__ == "__main__":
    unittest.main()
