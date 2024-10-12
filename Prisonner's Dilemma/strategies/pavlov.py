class Pavlov:
    def __init__(self):
        self.name = "Pavlov"
        self.strategy = "Moderate"
        self.own_history = []
        self.op_history = []
    
    def play(self, own_move, op_move, round):
        if round > 1:
            self.own_history.append(own_move)
            self.op_history.append(op_move)
        
        if round == 1:
            return 'C'  # Starts by cooperating
        elif own_move == op_move:
            return own_move  # Stay with cooperation if both cooperated
        else:
            return 'D' if own_move == 'C' else 'C'  # Defect if either player defected in the previous round
