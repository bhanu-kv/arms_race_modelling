class Resurection():
    def __init__(self):
        self.name = 'Resurection'
        self.strategy = 'Good'
        self.own_history = []
        self.op_history = []
    
    def play(self, own_move, op_move, round):
        if round == 1:
            return 'C'
        
        self.own_history.append(own_move)
        self.op_history.append(op_move)

        if len(self.own_history) >= 5 and self.own_history[-5:] == ['D', 'D', 'D', 'D', 'D']:
            return 'D'
        else:
            return self.op_history[-1]