from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dino_list = []
        self.create_herd()
    
    def create_herd(self):
        dino_1 = Dinosaur('Rex', 25)
        dino_2 = Dinosaur('raptor', 25)
        dino_3 = Dinosaur('steg', 25)

        self.dino_list.append(dino_1)
        self.dino_list.append(dino_2)
        self.dino_list.append(dino_3)

        