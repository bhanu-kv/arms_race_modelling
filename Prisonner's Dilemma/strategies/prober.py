class Prober:
    def __init__(self):
        self.name = "Prober"
        self.strategy = "Grim"  # Mixes cooperation and defection to assess opponent
        self.own_history = []
        self.op_history = []
    
    def play(self, own_move, op_move, round):
        if round == 1:
            return 'C'
        return 'C' if round % 4 != 0 else 'D'  # Defects every fourth round