import unittest
from Character import Character
from Location import Location
from World import World


class WorldTest(unittest.TestCase):
    def test_one_timestep(self):
        characters = []
        locations = []

        for i in range(5):
            characters.append(Character.random())
        for i in range(2):
            name = "house" + str(i)
            locations.append(Location(name))

        world = World(locations, characters)
        world.simulate(1)
        self.assertEqual(1, world.timestep)

    def test_multiple_timesteps(self):
        characters = []
        locations = []

        for i in range(5):
            characters.append(Character.random())
        for i in range(5):
            name = "house" + str(i)
            locations.append(Location(name))

        world = World(locations, characters)
        world.simulate(33)
        self.assertEqual(33, world.timestep)

    def test_multiple_simulations(self):
        characters = []
        locations = []

        for i in range(5):
            characters.append(Character.random())
        for i in range(5):
            name = "house" + str(i)
            locations.append(Location(name))

        world = World(locations, characters)
        world.simulate(33)
        world.simulate(35)
        self.assertEqual(68, world.timestep)


if __name__ == '__main__':
    unittest.main()
