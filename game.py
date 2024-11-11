# game.py
from files.player import Player
from files.room import Room
from story import Story

class Game:
    def __init__(self):
        self.player = Player()
        self.current_room = Room("Starting Room", "You are in a dimly lit room.")
        self.story = Story()

    def start(self):
        print(self.story.intro())
        while True:
            print(self.current_room.description)
            command = input("What do you want to do? ")
            if command.lower() == "quit":
                print("Thanks for playing!")
                break
            self.process_command(command)

    def process_command(self, command):
        # Process player commands here
        pass
