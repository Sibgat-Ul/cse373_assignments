class Node:
    def __init__(self, value):
        self.value = value
        self.color = 'white'

    def get_value(self):
        return self.value

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color