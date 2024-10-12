import random

class Alternator():
    def __init__(self):
        self.name = 'Alternator'
        self.strategy = 'Grim'
    
    def play(self, own_move, op_move, round):
        if own_move == 'start':
            if random.random() < 0.5:
                return 'C'
            else:
                return 'D'
        
        if own_move == 'C':
            return 'D'
        else:
            return 'C'