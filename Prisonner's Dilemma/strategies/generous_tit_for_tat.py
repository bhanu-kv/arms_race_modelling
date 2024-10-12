import random

class GenerousTitForTat:
    def __init__(self):
        self.name = "GenerousTitForTat"
        self.strategy = "Good"  # More forgiving version of Tit for Tat
        self.own_history = []
        self.op_history = []
    
    def play(self, own_move, op_move, round):
        if round > 1:
            self.own_history.append(own_move)
            self.op_history.append(op_move)
        if round == 1:
            return 'C'
        elif self.op_history[-1] == 'D':
            return 'C' if random.random() > 0.1 else 'D'  # Forgives 90% of defections
        else:
            return 'C'
