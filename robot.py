from weapon import Weapon

class Robot:
    def __init__(self,name):
        self.robo_name = name
        self.robo_health = 100
        self.robo_weapon = Weapon()
        self.attack_list = []

    
    def robo_attack(self, dinosaur):
        if self.robo_health > 1:
            while True:
                user_input = int(input(f'Choose your attack: (1) {self.robo_weapon[0]}, (2) {self.robo_weapon(1)}, or (3) {self.robo_weapon[2]}.  ')
                if user_input == 1:
                    print(f'{self.robo_name} attacked {dinosaur.type} with {self.attack_list[0]}')
                    break
                elif user_input == 2:
                    print(f'{self.robo_name} attacked {dinosaur.type} with {self.attack_list[1]}')
                    break
                elif user_input == 3:
                    print(f'{self.robo_name} attacked {dinosaur.type} with {self.attack_list[2]}')
                    break
                

            