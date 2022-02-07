from random import random
from herd import Herd
from fleet import Fleet

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welome()
        self.fleet_vs_herd_battle()
        user_team = self.pick_team
        self.dino_turn()
        self.robo_turn()
        
        

    def display_welome(self):
        print('Welcome to Robots vs Dinosaurs')
        print('Each character starts with 100 health')
        print("A fleet of robot invaders have come to sieze control of planet IIOOIO but the dinosaur herd aren't going down without a fight")
        print('Whoever remains at the end will be the victor')

    def pick_team(self):
        pick_team = int(input('Choose your team: (1) Robots; (2) Dinosaurs'))
        if pick_team == 1:
            print('You chose the fleet of Robots')
            return pick_team
        elif pick_team == 2:
            print('You chose the herd of Dinosaurs')
            return pick_team
        else:
            print('Your answer does not compute')
            self.pick_team()

            

    def fleet_vs_herd_battle(self):
        first_turn = random.randint(1, 2)
        if first_turn == 1:
            print('Robots are up first')
            first_turn = 1
        if first_turn == 2:
            print('Dinosaurs are up first')
            first_turn = 2

        if first_turn == 1:
            while len(self.fleet.robo_list) > 0 and len(self.herd.dino_list) > 0:
                if self.fleet.robo_list[0].robo_health > 0 or self.herd.dino_list[0].dino_health > 0:
                    self.dino_turn
                    return
        elif first_turn == 2:
            while len(self.fleet.robo_list) > 0 and len(self.herd.dino_list) > 0:
                    if self.fleet.robo_list[0].robo_health > 0 or self.herd.dino_list[0].dino_health > 0:
                        self.robo_turn
                        return
        
        
       

    def dino_turn(self, dinosaur):
        while self.fleet.robo_list[0].robo_health > 0:
            self.fleet.robo_list[0].robo_health - self.herd.dino_list[0].dino_attack
            print('you attacked for 25 damage')
            if self.fleet.robo_list[0].robo_health != 0:
                continue
            else:
                break
            
            

    def robo_turn(self, robot):
        while self.herd.dino_list[0].dino_health.robo_health > 0:
            self.herd.dino_list[0].dino_health - self.fleet.robo_list[0].robo_weapon
            print('You attacked for 25 damage')
            if self.herd.dino_list[0].dino_health != 0:
                continue
            else:
                break
        
    
    def show_dino_opponent_options(self):
        for dino in self.herd.dino_list:
            print(dino.dino_name)

    def show_robo_opponent_options(self):
        for robo in self.fleet.dino_list:
            print(robo.robo_name)
    
    def display_winners(self):
        if self.fleet.robo_list > self.herd.dino_list:
            print('The Robots have won!')
        elif self.herd.dino_list > self.fleet.robo_list:
            print('The Dinosaurs won!')
