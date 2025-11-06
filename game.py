import random


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
    def choose_random_monster(orc, goblin):
        monsters = [orc, goblin]
        game_monster = random.choice(monsters)
        return game_monster

    @staticmethod
    def roll_dice(sides):
        return random.randint(1, sides)

    @staticmethod
    def chek_first(player,monster):
        roll_p =  player.attack()["round"]
        print(roll_p)
        roll_m = monster.attack()["round"]
        print(roll_m)
        if roll_m > roll_p:
            return monster
        if roll_m < roll_p:
            return player
        else:
            return player

    # @staticmethod
    # def battle(player,monster):
    #     first = Game.chek_first(player,monster)


