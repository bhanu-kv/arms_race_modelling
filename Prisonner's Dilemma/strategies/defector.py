class Defector():
    def __init__(self):
        self.name = 'Defector'
        self.strategy = 'Grim'
    
    def play(self, own_move, op_move, round):
        return 'D'