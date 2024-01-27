import random
class card:
    def __init__(self, name, value, type):
        self.name = name
        self.value = value
        self.type = type

    def Right(self):
        text = "Your right it was the " + self.name + " of " + self.type
        print(text)

    def Wrong(self):
        text = "Your wrong it was the " + self.name + " of " + self.type
        print(text)


