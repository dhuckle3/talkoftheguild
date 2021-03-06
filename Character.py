import random
import names

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
        self.location = None

    @classmethod
    def random(cls):
        gender = random.choice(['male', 'female'])
        name = names.get_full_name(gender)
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

    def decay_relationship(self):
        for name in self.relationship.keys():
            self.relationship[name] = max([self.relationship[name] - 0.1, 0])

    def socialize(self, character):
        if not self.knows(character):
            self.relationship[character.name] = 0.0
            character.relationship[self.name] = 0.0
        character.relationship[self.name] += character.calculate_charge_increment(self)
        self.relationship[character.name] += self.calculate_charge_increment(character)

    def choose_character_to_socialize(self, characters):
        return random.choice(characters)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def display_relationships(self):
        print("{} has the following relationships:".format(self.name))
        for name in self.relationship.keys():
            charge = int(self.relationship[name])
            print("\t{} is {}({})".format(name, relationship_name(charge), charge))

def relationship_name(charge):
    if charge < -100:
        return "an enemy"
    elif charge < 100:
        return "an acquaintance"
    else:
        return "a friend"
