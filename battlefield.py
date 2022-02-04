from herd import Herd
from fleet import Fleet

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        print(self.fleet.robo_list[0].robo_weapon.weapon_name)
        
        

    def display_welome(self):
        print('Welcome to Robots vs Dinosaurs')
        print('Each character starts with 100 health')
        print("A fleet of robot invaders have come to sieze control of planet IIOOIO but the dinosaur herd aren't going down without a fight")
        print('Whoever remains at the end will be the victor')

        
    def fleet_vs_herd_battle(self):
        fleet_vs_herd_battle = int(input('choose your team: press 1 for robots or 2 for dinosaurs '))
        if fleet_vs_herd_battle == 1:
            print('You chose Robots!')
            return fleet_vs_herd_battle
        elif fleet_vs_herd_battle == 2:
            print('You chose Dinosaurs!')
            return fleet_vs_herd_battle
    
       

    def dino_turn(self, dinosaur):
        while len(self.herd.dino_health) > 1:
            pass
            
    def robo_turn(self, robot):
        pass
    
    def show_dino_opponent_options(self):
        for dino in self.herd.dino_list:
            print(dino.dino_name)

    def show_robo_opponent_options(self):
        for robo in self.fleet.dino_list:
            print(robo.robo_name)
    
    def display_winners(self):
        pass
