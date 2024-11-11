# player.py
class Player:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
