class Provocateur:
    def __init__(self):
        self.name = "Provocateur"
        self.strategy = "Grim"  # Attempts to provoke a defection from the opponent
        self.own_history = []
        self.op_history = []
    
    def play(self, own_move, op_move, round):
        if round == 1:
            return 'C'
        return 'D' if round % 3 == 0 else 'C'  # Defects every third round
