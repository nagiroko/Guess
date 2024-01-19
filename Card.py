class card:
    def __init__(self, name, value, type):
        self.name = name
        self.value = value
        self.type = type

    def Readout(self):
        text = self.name + " of " + self.type + "s"
        return text
