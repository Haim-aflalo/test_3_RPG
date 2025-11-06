from core import monster
import game
import random


class Goblin(monster.Monster):
    def __init__(self):
        super().__init__()
        self.name = "Bloorb"
        self.type = "goblin"
        self.hp = 20
        self.speed = random.randrange(5, 11)
        self.power = random.randrange(5, 11)
        self.armor_rating = 1

    def speak(self):
        print(f"Hi im {self.name} the {self.type}")

    def attack(self):
        player_attack = {
            "round": (game.Game.roll_dice(6) + self.speed),
            "shot": (game.Game.roll_dice(20) + self.speed),
            "damage": (game.Game.roll_dice(6) + self.power)
        }
        return player_attack

    def run_away(self):
        pass
