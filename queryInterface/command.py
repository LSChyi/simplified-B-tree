class Command:
    def __init__(self, name, description, usage, function):
        self.name = name
        self.description = description
        self.usage = usage
        self.function = function

    def doIt(self, *params):
        self.function(*params)

    def __str__(self):
        return "{}: {}".format(self.name, self.description)
