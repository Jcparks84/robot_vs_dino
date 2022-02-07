from robot import Robot
from robot import Robot

class Fleet:
    def __init__(self):
        self.robo_list = []
        self.create_fleet()

    def create_fleet(self):
        robot_1 = Robot('Darth Vader')
        robot_2 = Robot('Megatron')
        robot_3 = Robot('T 1000')

        self.robo_list.append(robot_1)
        self.robo_list.append(robot_2)
        self.robo_list.append(robot_3)