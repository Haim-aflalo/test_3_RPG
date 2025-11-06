import random
import game

class Player:

    def __init__(self):
        self.name = "Narnia"
        self.hp = 50
        self.speed = random.randrange(5, 11)
        self.power = random.randrange(5, 11)
        self.armor_rating = random.randrange(5, 16)
        self.profession = random.choice(["warrior", "healer"])

    def speak(self):
        print(f"Hi im {self.name} the {self.profession}")

    def attack(self):
        player_attack = {
            "round": (game.Game.roll_dice(6) + self.speed),
            "shot" : (game.Game.roll_dice(20)+self.speed),
            "damage" : (game.Game.roll_dice(6) + self.power)
        }
        return player_attack