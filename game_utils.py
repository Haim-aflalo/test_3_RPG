class Utils:


    @staticmethod
    def check_fighter(player,monster):
        roll_p =  player.attack()["round"]
        roll_m = monster.attack()["round"]
        if roll_m > roll_p:
            print("the monster shot")
            return False
        if roll_m < roll_p:
            print("the player shot")
            return True
        else:
            print("the player shot")
            return True

    @staticmethod
    def player_shot(first,player,monster):
        shot = player.attack()["shot"]
        if shot > monster.armor_rating:
            monster.hp -= player.attack()["damage"]
            first = first
        else:
            first = False


    @staticmethod
    def monster_shot(first,player,monster):
        shot = monster.attack()["shot"]
        damage = {"knife": 0.5, "hammer": 1.5, "sword":1}
        monster_damage =  monster.attack()["damage"]
        if shot > player.armor_rating:
            player.hp -= monster_damage*damage[monster.weapon]
            first = first
        else:
            first = True


