import random


class World:
    def __init__(self, locations, characters):
        self.locations = locations
        self.characters = characters
        self.timestep = 0

    def simulate(self, steps):
        for i in range(steps):
            self._simulate_step()

        for character in self.characters:
            print("{} has the following relationships:".format(character.name))
            character.display_relationships()

    def _simulate_step(self):
        """simulate a number of steps in the world"""

        self.timestep += 1
        print('Time', self.timestep)
        for character in self.characters:
            character.decay_relationship()
            if character.location is not None:
                character.location.characters.remove(character)
            location = random.choice(self.locations)
            location.characters.add(character)
            character.location = location

        for location in self.locations:
            for character in location.characters:
                characters_except_current = [c for c in location.characters if c.name != character.name]
                if len(characters_except_current) > 0:
                    other_character = character.choose_character_to_socialize(characters_except_current)
                    character.socialize(other_character)
                    print("{} socialized with {}.".format(character.name, other_character.name))