import random
import core.goblin
import core.orc
import game_utils


class Game:

    @staticmethod
    def start():
        return Game.show_menu()

    @staticmethod
    def show_menu():
        while True:
            choice = input("fight or exit (f/e)?")
            if choice not in ["f", "e"]:
                print("not in choices")
                continue
            else:
                return choice

    @staticmethod
    def choose_random_monster():
        orc  = core.orc.Orc()
        goblin = core.goblin.Goblin()
        monsters = [orc, goblin]
        game_monster = random.choice(monsters)
        return game_monster

    @staticmethod
    def roll_dice(sides):
        return random.randint(1, sides)

    @staticmethod
    def battle(first,player,monster):
            if first:
                game_utils.Utils.player_shot(first,player,monster)
            if not first:
                game_utils.Utils.monster_shot(first,player,monster)


