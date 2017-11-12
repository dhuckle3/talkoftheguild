import unittest
from Personality import Personality


class PersonalityTest(unittest.TestCase):
    def test_creation_with_traits(self):
        p1 = Personality(1.0, 1.0, 1.0, 0, -1.0)
        p2 = Personality(1.0, 1.0, 1.0, 0, -1.0)
        self.assertEqual(p1.compatibility(p2), 1.0)

    def test_compatibility_is_one_for_self(self):
        p1 = Personality.with_random_traits()
        self.assertEqual(p1.compatibility(p1), 1.0)

    def test_perfect_opposites_have_negative_one_similarity(self):
        p1 = Personality(1.0, 0, 1.0, 0, 1.0)

        p2 = Personality.with_random_traits()
        p2.agreeableness = -1.0
        p2.extraversion = -1.0
        p2.openness = -1.0

        self.assertEqual(p1.compatibility(p2), -1.0)


if __name__ == '__main__':
    unittest.main()
