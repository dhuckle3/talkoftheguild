import unittest

from Character import Character
from Personality import Personality


class CharacterTest(unittest.TestCase):

    def test_characters_know_each_other_after_socialization(self):
        alex = Character.random()
        alex.gender = 'male'
        amy = Character.random()
        amy.gender = 'female'
        self.assertFalse(amy.knows(alex))
        amy.socialize(alex)
        self.assertTrue(amy.knows(alex))

    def test_same_gender_is_same(self):
        male1 = Character.random()
        male1.gender = 'male'
        male2 = Character.random()
        male2.gender = 'male'
        self.assertTrue(male1.is_same_gender(male2))

    def test_different_gender_is_detected(self):
        male = Character.random()
        male.gender = 'male'
        female = Character.random()
        female.gender = 'female'
        self.assertFalse(male.is_same_gender(female))

    def test_calculate_charge_increment(self):
        male = Character.random()
        male.gender = 'male'
        male.age = 20
        male.personality = Personality(0, 0, 0, 0, 0)
        female = Character.random()
        female.gender = 'female'
        female.age = 20
        female.personality = Personality(0, 0, 0, 0, 0)
        self.assertEqual(0.9, male.calculate_charge_increment(female))

    def test_age_difference_affects_charge_increment(self):
        male1 = Character.random()
        male1.gender = 'male'
        male1.age = 10
        male1.personality = Personality(0, 0, 0, 0, 0)
        male2 = Character.random()
        male2.gender = 'male'
        male2.age = 20
        male2.personality = Personality(0, 0, 0, 0, 0)
        self.assertEqual(33, int(male1.calculate_charge_increment(male2)*100))

    def test_base_charge_increment(self):
        char1 = Character.random()
        char1.gender = 'male'
        char1.age = 10
        char1.personality = Personality(0, 0, 0, 0, 0)
        self.assertEqual(1.0, char1.calculate_charge_increment(char1))


    def test_extroversion_adds_to_charge_increment(self):
        char1 = Character.random()
        char1.gender = 'male'
        char1.age = 10
        char1.personality = Personality(0, 0, 1, 0, 0)
        char2 = Character.random()
        char2.gender = 'male'
        char2.age = 10
        char2.personality = Personality(0, 0, 1, 0, 0)
        self.assertEqual(2.0, char1.calculate_charge_increment(char2))

    def test_agreeableness_adds_to_charge_increment(self):
        char1 = Character.random()
        char1.gender = 'male'
        char1.age = 10
        char1.personality = Personality(1, 0, 0, 0, 0)
        char2 = Character.random()
        char2.gender = 'male'
        char2.age = 10
        char2.personality = Personality(1, 0, 0, 0, 0)
        self.assertEqual(2.0, char1.calculate_charge_increment(char2))

    def test_socialize_updates_both_characters_charge(self):
        char1 = Character.random()
        char2 = Character.random()

        char1_charge = char1.calculate_charge_increment(char2)
        char2_charge = char2.calculate_charge_increment(char1)
        char1.socialize(char2)

        self.assertEqual(char1_charge, char1.relationship[char2.name])
        self.assertEqual(char2_charge, char2.relationship[char1.name])





if __name__ == '__main__':
    unittest.main()
