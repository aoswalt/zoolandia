class Habitat(object):
    def __init__(self):
        self.name = ""
        self.members = set()

    def add_member(self, animal):
        self.members.add(animal)

    def remove_member(self, animal):
        self.members.discard(animal)


class Aquarium(Habitat):
    def __init__(self, water_type):
        Habitat.__init__(self)
        self.water_type = water_type
