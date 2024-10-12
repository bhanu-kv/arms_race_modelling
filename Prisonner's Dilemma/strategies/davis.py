class Davis():
    def __init__(self):
        self.name = 'Davis'
        self.strategy = 'Good'
    
    def play(self, own_move, op_move, round):
        if round <= 10:
            return 'C'
        else:
            return op_move