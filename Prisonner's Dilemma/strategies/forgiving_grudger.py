class ForgivingGrudger:
    def __init__(self):
        self.name = "ForgivingGrudger"
        self.strategy = "Moderate"  # Will return to cooperation after defections
        self.own_history = []
        self.op_history = []
        self.triggered = False
        self.punishment_timer = 0
    
    def play(self, own_move, op_move, round):
        if round > 1:
            self.own_history.append(own_move)
            self.op_history.append(op_move)
        if round == 1:
            return 'C'
        if self.op_history[-1] == 'D':
            self.triggered = True
            self.punishment_timer = 2  # Punish for 2 rounds
        if self.punishment_timer > 0:
            self.punishment_timer -= 1
            return 'D'
        return 'C'
