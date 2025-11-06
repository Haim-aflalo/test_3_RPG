import game
from core import player
import game_utils

def play():
    this_game = game.Game()
    game_player = player.Player()
    game_monster = this_game.choose_random_monster()
    game_player.speak()
    game_monster.speak()
    while True:
        if this_game.start() == "f":
            game_player.attack()
            game_monster.attack()
            first = game_utils.Utils.check_fighter(game_player, game_monster)
            this_game.battle(first,game_player,game_monster)
            if game_player.chek_hp():
                print(game_player.hp)
                print(game_monster.hp)
                print("THE MONSTER WON")
                break
            if game_monster.chek_hp():
                print(game_player.hp)
                print(game_monster.hp)
                print("THE PLAYER WON")
                break
            print(game_player.hp)
            print(game_monster.hp)
            continue
        else:
            print("Running...")
            break

if __name__ == "__main__":
    play()




