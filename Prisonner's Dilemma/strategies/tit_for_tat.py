class TitForTat():
    def __init__(self):
        self.name = 'TitForTat'
        self.strategy = 'Good'
        self.own_history = []
        self.op_history = []
    
    def play(self, own_move, op_move, round):
        if own_move == 'start':
            return 'C'

        self.op_history.append(op_move)
        return self.op_history[-1]