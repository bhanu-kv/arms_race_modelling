import random

class Random():
    def __init__(self):
        self.name = 'Random'
        self.strategy = 'Grim'
    
    def play(self, own_move, op_move, round):
        if random.random() > 0.5:
            return 'C'
        
        return 'D'