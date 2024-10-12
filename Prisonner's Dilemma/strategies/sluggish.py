class Sluggish:
    def __init__(self):
        self.name = "Sluggish"
        self.strategy = "Good"  # Responds to defections but with a delay
        self.own_history = []
        self.op_history = []
        self.defection_response = False
    
    def play(self, own_move, op_move, round):
        if round > 1:
            self.own_history.append(own_move)
            self.op_history.append(op_move)
        
        if round == 1:
            return 'C'
        
        if self.op_history[-1] == 'D':
            self.defection_response = True
            
        return 'D' if self.defection_response and round > 2 else 'C'
