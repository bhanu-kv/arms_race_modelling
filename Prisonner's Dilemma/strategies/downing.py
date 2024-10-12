class Downing():
    def __init__(self):
        self.name = 'Downing'
        self.strategy = 'Moderate'
        self.op_history = []
        self.own_history = []
        self.number_opponent_C_in_response_to_C = 0
        self.number_opponent_C_in_response_to_D = 0

        self.cooperations = 0
        self.defections = 0
    
    def play(self, own_move, op_move, round):
        """Actual strategy definition that determines player's action."""

        if round == 1:
            return 'D'
        
        self.own_history.append(own_move)
        self.op_history.append(op_move)

        if round == 2:
            if self.op_history[-1] == 'C':
                self.number_opponent_C_in_response_to_C += 1
            return 'D'

        if self.own_history[-2] == 'C' and self.op_history[-1] == 'C':
            self.number_opponent_C_in_response_to_C += 1
        if self.own_history[-2] == 'D' and self.op_history[-1] == 'C':
            self.number_opponent_C_in_response_to_D += 1

        # Adding 1 to cooperations for assumption that first opponent move
        # being a response to a cooperation. See docstring for more
        # information.
        alpha = self.number_opponent_C_in_response_to_C / (
            self.cooperations + 1
        )
        # Adding 2 to defections on the assumption that the first two
        # moves are defections, which may not be true in a noisy match
        beta = self.number_opponent_C_in_response_to_D / max(
            self.defections, 2
        )
        expected_value_of_cooperating = alpha * 3 + (1 - alpha) * 0
        expected_value_of_defecting = beta * 4 + (1 - beta) * 1

        if expected_value_of_cooperating > expected_value_of_defecting:
            return 'C'
        if expected_value_of_cooperating < expected_value_of_defecting:
            return 'D'
        return self.own_history[-1].flip()