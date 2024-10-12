class ContriteTitForTat:
    def __init__(self):
        self.name = "ContriteTitForTat"
        self.strategy = "Good"  # Tends to cooperate but acknowledges accidental defections
        self.own_history = []
        self.op_history = []
        self.punishment = False
    
    def play(self, own_move, op_move, round):
        if round > 1:
            self.own_history.append(own_move)
            self.op_history.append(op_move)
        if round == 1:
            return 'C'
        elif self.punishment:
            self.punishment = False
            return 'C'
        elif self.op_history[-1] == 'D' and own_move == 'D':
            self.punishment = True
            return 'D'
        else:
            return self.op_history[-1]
