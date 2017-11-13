import random

from Personality import Personality


class Character:
    """A character in the game world"""
    def __init__(self, name, gender, personality, age, occupation):
        self.age = age
        self.gender = gender
        self.name = name
        self.occupation = occupation
        self.personality = personality
        self.relationship = {}

    @classmethod
    def random(cls):
        name = ''.join(random.choice('abcde') for _ in range(3))
        gender = random.choice(['male', 'female', 'other'])
        personality = Personality.with_random_traits()
        age = random.randint(1, 100)
        occupation = random.choice(['farmer', 'adventurer', 'noble', None])
        return cls(name, gender, personality, age, occupation)

    def is_same_gender(self, character):
        return self.gender is character.gender

    def knows(self, character):
        return character.name in self.relationship

    def calculate_charge_increment(self, character):
        increment = self.personality.compatibility(character.personality)

        # extraversion give bonus to charge
        increment += self.personality.extraversion

        # agreeable people are easier to get to know
        increment += character.personality.agreeableness

        # different genders have slight penalty to socialization
        if not self.is_same_gender(character):
            increment -= 0.1

        # age difference reduces charge
        if self.age != character.age:
            increment -= (1 - abs(self.age - character.age) / (self.age + character.age))

        return increment

    def socialize(self, character):
        if not self.knows(character):
            self.relationship[character.name] = 0.0
            character.relationship[self.name] = 0.0
        character.relationship[self.name] += character.calculate_charge_increment(self)
        self.relationship[character.name] += self.calculate_charge_increment(character)
