import game
from core import player,orc,goblin

p = player.Player()
o= orc.Orc()
m = goblin.Goblin()
g = game.Game()
gm =  g.choose_random_monster(o,m)
print(g.chek_first(p,gm).type)
print(o.speed)