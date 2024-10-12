class TitForTwoTats:
    def __init__(self):
        self.name = "TitForTwoTats"
        self.strategy = "Good"  # A forgiving strategy, allows some defection before retaliating
        self.own_history = []
        self.op_history = []
    
    def play(self, own_move, op_move, round):
        if round > 1:
            self.own_history.append(own_move)
            self.op_history.append(op_move)
        if round == 1:
            return 'C'
        elif len(self.op_history) >= 2 and self.op_history[-1] == 'D' and self.op_history[-2] == 'D':
            return 'D'
        else:
            return 'C'
