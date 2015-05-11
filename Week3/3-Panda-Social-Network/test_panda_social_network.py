from class_panda import Panda
from panda_social_network import PandaSocialNetwork, PandaAlreadyThere, PandasAlreadyFriends
import unittest

class TestPandaSocialNetwork(unittest.TestCase):


    def test_add_panda(self):
        socialPanda = PandaSocialNetwork({})

        with self.assertRaises(PandaAlreadyThere):
            ivo = Panda("Ivo", "ivo@pandamail.com", "male")
            socialPanda.add_panda(ivo)
            socialPanda.add_panda(ivo)

    def test_has_panda(self):
        socialPanda = PandaSocialNetwork({})
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        rado = Panda("Rado", "rado@pandamail.com", "male")
        filip = Panda("Fil", "fil@pandamail.com", "male")
        socialPanda.add_panda(ivo)
        socialPanda.add_panda(rado)
        self.assertTrue(socialPanda.has_panda(rado))
        self.assertFalse(socialPanda.has_panda(filip))

    def test_make_friends(self):
        socialPanda = PandaSocialNetwork({})
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        rado = Panda("Rado", "rado@pandamail.com", "male")
        with self.assertRaises(PandasAlreadyFriends):
            socialPanda.make_friends(ivo, rado)
            socialPanda.make_friends(ivo, rado)

    def test_are_friends(self):
        socialPanda = PandaSocialNetwork({})
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        rado = Panda("Rado", "rado@pandamail.com", "male")
        self.assertFalse(socialPanda.are_friends(ivo, rado))
        socialPanda.make_friends(ivo, rado)
        self.assertTrue(socialPanda.are_friends(ivo, rado))

    def test_friend_of(self):
        socialPanda = PandaSocialNetwork({})
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        rado = Panda("Rado", "rado@pandamail.com", "male")
        fil = Panda("Fil", "fil@pandamail.com", "male")
        hack = Panda("Hack", "hack@pandamail.com", "male")
        emo = Panda("Emo", "emo@pandamail.com", "male")
        socialPanda.make_friends(ivo, rado)
        socialPanda.make_friends(ivo, fil)
        socialPanda.make_friends(ivo, hack)
        self.assertFalse(socialPanda.friend_of(emo))
        friends_of_ivo = []
        for pandas in socialPanda.friend_of(ivo):
            friends_of_ivo.append(pandas)
        self.assertEqual(socialPanda.friend_of(ivo), friends_of_ivo)

    def test_connection_level(self):
        socialPanda = PandaSocialNetwork({})
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        rado = Panda("Rado", "rado@pandamail.com", "male")
        fil = Panda("Fil", "fil@pandamail.com", "male")
        hack = Panda("Hack", "hack@pandamail.com", "male")
        bambi = Panda("Bambi", "bambi@pandamail.com", "female")
        spindi = Panda("Spindi", "spindi@pandamail.com", "male")
        mecupug = Panda("Meco Pug", "mecopug@pandamail.com", "male")
        metodi = Panda("Metodi", "metodi@pandamail.com", "male")
        ganio = Panda("Ganio", "ganio@pandamail.com", "male")
        socialPanda.make_friends(ivo, rado)
        socialPanda.make_friends(ivo, fil)
        socialPanda.make_friends(ivo, bambi)
        socialPanda.make_friends(spindi, mecupug)
        socialPanda.make_friends(rado, metodi)
        socialPanda.make_friends(metodi, ganio)
        socialPanda.make_friends(fil, ganio)
        friends_level = 1
        are_not_connected = -1
        shortest_path = socialPanda.connection_level(ivo, ganio)
        """
        ganio = path_to[ganio] = fil #1
        fil = path_to[fil] = ivo #2
        ivo = path_to[ivo] = None
        connection_level = 2
        """
        shortest_path2 = socialPanda.connection_level(bambi, metodi)
        """
        metodi = path_to[metodi] = rado #1
        rado = path_to[rado] = ivo #2
        ivo = path_to[ivo] = bambi #3
        bambi = path_to[bambi] = None
        connection_level = 3
        """
        self.assertEqual(socialPanda.connection_level(ivo, rado), friends_level)
        self.assertFalse(socialPanda.connection_level(ivo, hack))
        self.assertEqual(socialPanda.connection_level(ivo, spindi), are_not_connected)
        self.assertEqual(shortest_path, 2)
        self.assertEqual(shortest_path2, 3)

    def test_are_connected(self):
        socialPanda = PandaSocialNetwork({})
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        rado = Panda("Rado", "rado@pandamail.com", "male")
        fil = Panda("Fil", "fil@pandamail.com", "male")
        hack = Panda("Hack", "hack@pandamail.com", "male")
        bambi = Panda("Bambi", "bambi@pandamail.com", "female")
        spindi = Panda("Spindi", "spindi@pandamail.com", "male")
        mecupug = Panda("Meco Pug", "mecopug@pandamail.com", "male")
        metodi = Panda("Metodi", "metodi@pandamail.com", "male")
        ganio = Panda("Ganio", "ganio@pandamail.com", "male")
        socialPanda.make_friends(ivo, rado)
        socialPanda.make_friends(ivo, fil)
        socialPanda.make_friends(ivo, bambi)
        socialPanda.make_friends(spindi, mecupug)
        socialPanda.make_friends(rado, metodi)
        socialPanda.make_friends(metodi, ganio)
        socialPanda.make_friends(fil, ganio)

        self.assertTrue(socialPanda.are_connected(ivo, rado))
        self.assertTrue(socialPanda.are_connected(ivo, ganio))
        self.assertFalse(socialPanda.are_connected(ivo, hack))
        self.assertFalse(socialPanda.are_connected(ivo, mecupug))


    def test_how_many_gender_in_network(self):
        socialPanda = PandaSocialNetwork({})
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        rado = Panda("Rado", "rado@pandamail.com", "male")
        fil = Panda("Fil", "fil@pandamail.com", "male")
        hack = Panda("Hack", "hack@pandamail.com", "male")
        bambi = Panda("Bambi", "bambi@pandamail.com", "female")
        spindi = Panda("Spindi", "spindi@pandamail.com", "male")
        mecupug = Panda("Meco Pug", "mecopug@pandamail.com", "male")
        metodi = Panda("Metodi", "metodi@pandamail.com", "male")
        ganio = Panda("Ganio", "ganio@pandamail.com", "male")
        emo = Panda("Emo", "emo@pandamail.com", "male")
        natalia = Panda("Natalia", "natalia@pandamail.com", "female")
        martina = Panda("Martina", "martina@pandamail.com", "female")
        socialPanda.make_friends(ivo, rado)
        socialPanda.make_friends(ivo, fil)
        socialPanda.make_friends(ivo, bambi)
        socialPanda.make_friends(spindi, mecupug)
        socialPanda.make_friends(rado, metodi)
        socialPanda.make_friends(metodi, ganio)
        socialPanda.make_friends(fil, ganio)
        socialPanda.make_friends(emo, natalia)
        socialPanda.make_friends(emo, martina)
        socialPanda.make_friends(emo, ganio)
        result = socialPanda.how_many_gender_in_network(2, ivo, "male")
        """
        ivo[rado, fil, bambi] # 2
        rado[ivo, metodi] # 1
        fil[ganio,ivo] # 1
        bambi[ivo] # 0
        result = 4
        """
        self.assertEqual(socialPanda.how_many_gender_in_network(2, ivo, "male"), result)
        result2 = socialPanda.how_many_gender_in_network(3, ivo, "male")
        """
        ivo[rado, fil, bambi] # 2
        rado[ivo, metodi] # 1
        fil[ganio,ivo] # 1
        bambi[ivo] # 0
        metodi[rado, ganio] # 0
        ganio[fil, metodi, emo] # 1
        result = 5
        """
        self.assertEqual(socialPanda.how_many_gender_in_network(3, ivo, "male"), result2)
        result3 = socialPanda.how_many_gender_in_network(4, ivo, "female")
        """
        ivo[rado, fil, bambi] # 1
        rado[ivo, metodi] # 0
        fil[ganio,ivo] # 0
        bambi[ivo] # 0
        metodi[rado, ganio] # 0
        ganio[fil, metodi, emo] #
        emo[natalia, martina, ganio] # 2
        result = 3
        """
        self.assertEqual(socialPanda.how_many_gender_in_network(4, ivo, "female"), result3)

    def test_save_social_network(self):
                 socialPanda = PandaSocialNetwork({})
                 ivo = Panda("Ivo", "ivo@pandamail.com", "male")
                 rado = Panda("Rado", "rado@pandamail.com", "male")
                 fil = Panda("Fil", "fil@pandamail.com", "male")
                 hack = Panda("Hack", "hack@pandamail.com", "male")
                 bambi = Panda("Bambi", "bambi@pandamail.com", "female")
                 spindi = Panda("Spindi", "spindi@pandamail.com", "male")
                 mecupug = Panda("Meco Pug", "mecopug@pandamail.com", "male")
                 metodi = Panda("Metodi", "metodi@pandamail.com", "male")
                 ganio = Panda("Ganio", "ganio@pandamail.com", "male")
                 emo = Panda("Emo", "emo@pandamail.com", "male")
                 natalia = Panda("Natalia", "natalia@pandamail.com", "female")
                 martina = Panda("Martina", "martina@pandamail.com", "female")
                 socialPanda.make_friends(ivo, rado)
                 socialPanda.make_friends(ivo, fil)
                 socialPanda.make_friends(ivo, bambi)
                 socialPanda.make_friends(spindi, mecupug)
                 socialPanda.make_friends(rado, metodi)
                 socialPanda.make_friends(metodi, ganio)
                 socialPanda.make_friends(fil, ganio)
                 socialPanda.make_friends(emo, natalia)
                 socialPanda.make_friends(emo, martina)
                 socialPanda.make_friends(emo, ganio)
                 socialPanda.save_social_network(socialPanda.prepare_to_json())

    def test_load_social_network(self):

        socialPanda = PandaSocialNetwork({})
        network = socialPanda.load_social_network("social_network.json")
        for content in network:
            print(content)


if __name__ == "__main__":
    unittest.main()
