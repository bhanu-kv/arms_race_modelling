import random

class BetterAndBetter():
    def __init__(self):
        self.name = 'BetterAndBetter'
        self.strategy = 'Moderate'
        self.own_history = []
        self.op_history = []
        self.op_cooperations = 0
    
    def play(self, own_move, op_move, round):
        """Actual strategy definition that determines player's action."""
        if round == 1:
            return 'D'
        
        self.own_history.append(own_move)
        self.op_history.append(op_move)

        p = len(self.op_history) / 100
        
        if random.random() < p:
            return 'D'
        else:
            return 'C'