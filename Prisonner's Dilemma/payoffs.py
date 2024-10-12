class PayOffMatrix():
    def __init__(self, default=True):
        self.default = default
        self.default_payoff = {('C', 'C'): [3, 3],
                       ('C', 'D'): [0, 5],
                       ('D', 'C'): [5, 0],
                       ('D', 'D'): [1, 1]
                       }
    
    def return_payoff(self):
        if self.default == True:
            return self.default_payoff
        else:
            return self.user_define()

    def user_define(self):
        user_payoff = {}

        user_payoff[('C', 'C')] = input('What is the payoff for Cooperation and Cooperation?')
        user_payoff[('C', 'D')] = input('What is the payoff for Cooperation and Defection?')
        user_payoff[('D', 'C')] = input('What is the payoff for Defection and Cooperation?')
        user_payoff[('D', 'D')] = input('What is the payoff for Defection and Defection?')

        return user_payoff