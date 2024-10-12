class BenevolentTitan:
    def __init__(self):
        self.name = "Benevolent Titan"
        self.strategy = "Good"  # Starts with cooperation and continues unless overly provoked
        self.own_history = []
        self.op_history = []
        self.defections = 0
    
    def play(self, own_move, op_move, round):
        if round > 1:
            self.own_history.append(own_move)
            self.op_history.append(op_move)
        if round == 1:
            return 'C'
        if self.op_history[-1] == 'D':
            self.defections += 1
            return 'C' if self.defections < 3 else 'D'  # Returns to cooperation after some time
        return 'C'
