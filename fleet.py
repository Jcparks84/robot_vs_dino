from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.dino_list = ['']
        self.create_fleet()

    def create_fleet(self):
        weapon_1 = Weapon('lightsabre', 30)
        weapon_2 = Weapon('photon cannon', 20)
        weapon_3 = Weapon('mimetic polyalloy', 25)

        robot_1 = Robot('Darth Vader', weapon_1)
        robot_2 = Robot('Megatron', weapon_2)
        robot_3 = Robot('T 1000', weapon_3)

        self.robots.append(robot_1)
        self.robots.append(robot_2)
        self.robots.append(robot_3)