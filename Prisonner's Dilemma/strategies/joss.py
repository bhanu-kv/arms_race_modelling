import random

class Joss:
    def __init__(self):
        self.name = "Joss"
        self.strategy = "Grim"  # Mostly cooperative, but adds random defections
        self.own_history = []
        self.op_history = []
    
    def play(self, own_move, op_move, round):
        if round > 1:
            self.own_history.append(own_move)
            self.op_history.append(op_move)
        if round == 1:
            return 'C'
        else:
            if random.random() < 0.1:
                return 'D'  # 10% chance of defection regardless of opponent's move
            return self.op_history[-1]
