from weapon import Weapon

class Robot:
    def __init__(self,name):
        self.robo_name = name
        self.robo_health = 10
        self.robo_weapon = Weapon('lightsaber',10)
    
    def robo_attack(self, dinosaur):
        pass
    