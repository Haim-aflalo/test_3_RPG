from core import monster
import game
import random


class Orc(monster.Monster):
    def __init__(self):
        super().__init__()
        self.name = "Groorg"
        self.type = "orc"
        self.hp = 50
        self.speed = random.randrange(0, 6)
        self.power = random.randrange(10, 16)
        self.armor_rating = random.randrange(2, 9)

    def speak(self):
        print(f"Hi im {self.name} the {self.type}")

    def attack(self):
        player_attack = {
            "round": (game.Game.roll_dice(6) + self.speed),
            "shot": (game.Game.roll_dice(20) + self.speed),
            "damage": (game.Game.roll_dice(6) + self.power)
        }
        return player_attack
