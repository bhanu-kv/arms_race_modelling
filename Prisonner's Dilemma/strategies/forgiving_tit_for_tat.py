import random

class ForgivingTitForTat:
    def __init__(self):
        self.name = "ForgivingTitForTat"
        self.strategy = "Good"  # Cooperates more often, forgives defections
        self.own_history = []
        self.op_history = []
    
    def play(self, own_move, op_move, round):
        if round > 1:
            self.own_history.append(own_move)
            self.op_history.append(op_move)
        if round == 1:
            return 'C'
        elif self.op_history[-1] == 'D':
            return 'C' if random.random() > 0.2 else 'D'  # Forgives 80% of defections
        else:
            return 'C'
