from weapon import Weapon

class Robot:
    def __init__(self,name):
        self.robo_name = name
        self.robo_health = 100
        self.robo_weapon = Weapon('lightsabre', 25)

    
    def robo_attack(self, dinosaur):
        dinosaur.dino_health -= self.robo_weapon.weapon_attack_power
                

            