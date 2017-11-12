from random import uniform


class Personality:
    """Personalities are made up of he five personality traits as described here:
    https://en.wikipedia.org/wiki/Big_Five_personality_traits"""

    def __init__(self, agreeableness, conscientiousness, extraversion, neuroticism, openness):
        """Each of the five traits should be in the range -1.0 to 1.0"""
        self.agreeableness = agreeableness
        self.conscientiousness = conscientiousness
        self.extraversion = extraversion
        self.neuroticism = neuroticism
        self.openness = openness

    @classmethod
    def with_random_traits(cls):
        """Create a personality with random traits"""
        return cls(uniform(-1, 1), uniform(-1, 1), uniform(-1, 1), uniform(-1, 1), uniform(-1, 1))

    def compatibility(self, other):
        """Calculate average difference between the agreeableness, extroversion, and openness of the two personalities.
        A positive value indicates a higher compatibility. 1.0 and -1.0 indicate perfectly compatible and incompatible
        personalities respectively.

        :returns a floating point number in the range [-1.0 and 1.0]"""

        agreeable = abs(self.agreeableness - other.agreeableness)
        extroversion = abs(self.extraversion - other.extraversion)
        openness = abs(self.openness - other.openness)
        return -1 * (agreeable + extroversion + openness - 3) / 3
