class Dinosaur:
    def __init__(self, name, attack_power):
        self.dino_name = name
        self.dino_attack = attack_power
        self.dino_health = 100
        self.attack_list = ['bite', 'claw', 'stomp']


    def set_dino_attack(self, robot):
        if self.dino_health > 1:
            while True:
                user_input = int(input(f'Choose your attack: (1) {self.attack_list[0]}, (2) {self.attack_list[1]}, or (3) {self.attack_list}'))
                if user_input == 1:
                    print(f'{self.dino_name} attacked {robot.type} with {self.attack_list[0]}')
                    break
                elif user_input == 2:
                    print(f'{self.dino_name} attacked {robot.type} with {self.attack_list[1]}')
                    break
                elif user_input == 3:
                    print(f'{self.dino_name} attacked {robot.type} with {self.attack_list[2]}')
                    break
            
            
            