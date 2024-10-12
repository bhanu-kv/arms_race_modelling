import random

class AverageCopier():
    def __init__(self):
        self.name = 'AverageCopier'
        self.strategy = 'Good'
        self.own_history = []
        self.op_history = []
        self.op_cooperations = 0
    
    def play(self, own_move, op_move, round):
        """Actual strategy definition that determines player's action."""
        if round == 1:
            k = random.randint(0, 1)

            if k == 1:
                return 'C'
            else:
                return 'D'
        
        self.own_history.append(own_move)
        self.op_history.append(op_move)

        if op_move == 'C':
            self.op_cooperations += 1

        p = self.op_cooperations / len(self.op_history)
        
        if random.random() > p:
            return 'D'
        else:
            return 'C'