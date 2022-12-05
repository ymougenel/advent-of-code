class Pile:
    def __init__(self):
        self.content = []

    def stack(self, element):
        self.content.append(element)

    def destack(self):
        return self.content.pop(-1)

    def is_empty(self):
        return self.content == []

    def reverse(self):
        self.content.reverse()
