class Contrarian:
    def __init__(self):
        self.name = "Contrarian"
        self.strategy = "Grim"  # Always does the opposite of what the opponent does
        self.own_history = []
        self.op_history = []
    
    def play(self, own_move, op_move, round):
        if round == 1:
            return 'C'
        
        self.own_history.append(own_move)
        self.op_history.append(op_move)
        
        return 'D' if self.op_history[-1] == 'C' else 'C'
