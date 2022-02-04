from random import random
from herd import Herd
from fleet import Fleet

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        print(self.fleet.robo_list[0].robo_weapon.weapon_name)

        self.fleet.robo_list[0].robo_attack(self.herd.dino_list[0])
        

    def display_welome(self):
        print('Welcome to Robots vs Dinosaurs')
        print('Each character starts with 100 health')

        
    def fleet_vs_herd_battle(self):
        print("A fleet of robot invaders have come to sieze control of planet IIOOIO but the dinosaur herd aren't going down without a fight")
        print('Whoever remains at the end will be the victor')
       

    def dino_turn(self, dinosaur):
        pass
        

    def robo_turn(self, robot):
        pass
    
    def show_dino_opponent_options(self):
        for dino in self.herd.dino_list:
            print(dino.dino_name)

    def show_robo_opponent_options(self):
        pass
    
    def display_winners(self):
        pass
