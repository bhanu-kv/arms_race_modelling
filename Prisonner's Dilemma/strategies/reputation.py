import random

class Reputation:
    def __init__(self):
        self.name = "Reputation"
        self.strategy = "Good"  # Adjusts cooperation based on perceived opponent reputation
        self.own_history = []
        self.op_history = []
        self.cooperation_level = 0.5  # Initial cooperation level
    
    def play(self, own_move, op_move, round):
        if round > 1:
            self.own_history.append(own_move)
            self.op_history.append(op_move)
            if self.op_history[-1] == 'C':
                self.cooperation_level = min(1, self.cooperation_level + 0.1)
            else:
                self.cooperation_level = max(0, self.cooperation_level - 0.1)
        if round == 1:
            return 'C'
        return 'C' if random.random() < self.cooperation_level else 'D'
