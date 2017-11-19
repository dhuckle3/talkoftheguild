class Location:
    """representation of locations in the game world"""
    def __init__(self, name):
        self.name = name
        self.characters = set()

    def __repr__(self):
        return self.name