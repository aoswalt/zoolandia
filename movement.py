class Walking(object):
    def __init__(self):
        self.legs = 0
        self.walk_speed = 0

    def __str__(self):
        return "walking"


class Swimming(object):
    def __init__(self):
        self.fins = False
        self.flippers = False
        self.web_feet = False
        self.swim_speed = 0

    def __str__(self):
        return "swimming"


class Flying(object):
    def __init__(self):
        self.wings = 0
        self.air_speed = 0
        self.wingspan = 0

    def __str__(self):
        return "flying"
