class GrimTrigger:
    def __init__(self):
        self.name = "GrimTrigger"
        self.strategy = "Grim"  # Grim strategies involve long-term punishment for defection
        self.own_history = []
        self.op_history = []
        self.triggered = False
    
    def play(self, own_move, op_move, round):
        if round > 1:
            self.own_history.append(own_move)
            self.op_history.append(op_move)
        if round > 1 and self.op_history[-1] == 'D':
            self.triggered = True
        return 'D' if self.triggered else 'C'
