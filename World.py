import random


class World:
    def __init__(self, locations, characters):
        self.locations = locations
        self.characters = characters
        self.timestep = 0

    def simulate(self, steps):
        """simulate a number of steps in the world"""
        for i in range(steps):
            self.simulate_step()

    def display_state(self):
        for character in self.characters:
            character.display_relationships()

    def simulate_step(self):
        self.timestep += 1
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