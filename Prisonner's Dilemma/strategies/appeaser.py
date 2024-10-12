class Appeaser():
    def __init__(self):
        self.name = 'Appeaser'
        self.strategy = 'Good'
        self.own_history = []
        self.op_history = []
    
    def play(self, own_move, op_move, round):
        if round == 1:
            return 'C'
        else:
            self.own_history.append(own_move)
            self.op_history.append(op_move)

            if self.op_history[-1] == 'D':
                if self.own_history[-1] == 'C':
                    return 'D'
                else:
                    return 'C'
