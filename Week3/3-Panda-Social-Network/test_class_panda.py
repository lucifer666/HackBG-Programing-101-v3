from class_panda import Panda, EmailError
import unittest


class TestPanda(unittest.TestCase):

    def test_init(self):
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertEqual(ivo.name(), "Ivo")
        self.assertEqual(ivo.email(), "ivo@pandamail.com")
        self.assertEqual(ivo.gender(), "male")

    def test_name(self):
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertEqual(ivo.name(), "Ivo")

    def test_email(self):
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertEqual(ivo.email(), "ivo@pandamail.com")

    def test_gender(self):
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertEqual(ivo.gender(), "male")

    def test_isMale(self):
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertTrue(ivo.isMale())

    def test_isFemale(self):
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertFalse(ivo.isFemale())

    def test_eq(self):
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        ivo_copy = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertTrue(ivo == ivo_copy)

    def test_str(self):
         ivo = Panda("Ivo", "ivo@pandamail.com", "male")
         result = "I am Ivo. My email is ivo@pandamail.com. My gender is male."
         self.assertEqual(str(ivo), result)

    def test_hash(self):
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        result = hash(ivo)
        self.assertTrue(isinstance(result, int))

    def test_valid_mail(self):
        ivo = Panda("Ivo", "ivo#pandamail.com", "male")
        with self.assertRaises(EmailError):
            ivo.is_valid_email()

if __name__ == "__main__":
    unittest.main()
