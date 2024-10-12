import matplotlib.pyplot as plt
from payoffs import PayOffMatrix
from strategies.tit_for_tat import TitForTat
from strategies.defector import Defector
from strategies.alternator import Alternator
from strategies.better_and_better import BetterAndBetter
import random

class Game():
    def __init__(self, player1, player2, payoff, rounds, visualize = False, noise = 0):
        self.p1 = player1
        self.p2 = player2
        self.rounds = rounds
        self.payoff = payoff
        self.visualize = visualize
        self.noise = noise
    
    def play(self):
        p1_score = 0
        p2_score = 0

        p1_history = []
        p2_history = []

        p1Move = self.p1.play(own_move = 'start', op_move = 'C', round = 1)
        p2Move = self.p2.play(own_move = 'start', op_move = 'C', round = 1)

        for round in range(2, self.rounds+1):
            if p1Move == 'C' and p2Move =='C':  
                p1_score += self.payoff['C', 'C'][0]
                p2_score += self.payoff['C', 'C'][1]

            elif p1Move == 'C' and p2Move =='D':
                p1_score += self.payoff['C', 'D'][0]
                p2_score += self.payoff['C', 'D'][1]

            elif p1Move == 'D' and p2Move =='C':
                p1_score += self.payoff['D', 'C'][0]
                p2_score += self.payoff['D', 'C'][1]
            
            elif p1Move == 'D' and p2Move =='D':
                p1_score += self.payoff['D', 'D'][0]
                p2_score += self.payoff['D', 'D'][1]
            
            p1_history.append(p1Move)
            p2_history.append(p2Move)

            prev_p1Move = p1Move
            prev_p2Move = p2Move

            if random.random() < self.noise:
                if random.random() < 0.5:
                    if prev_p1Move == 'C':
                        prev_p1Move = 'D'
                else:
                    if prev_p2Move == 'C':
                        prev_p2Move = 'D'
            
            p1Move = self.p1.play(prev_p1Move, prev_p2Move, round)
            p2Move = self.p2.play(prev_p2Move, prev_p1Move, round)
        
        self.visualize_result(self.visualize, p1_history=p1_history, p2_history=p2_history)
    
        if self.visualize == True:
            if p1_score>p2_score:
                print(self.p1.name(),'beats',self.p2.name(),p1_score,'-',p2_score)
            elif p2_score>p1_score:    
                print(self.p2.name(),'beats',self.p1.name(),p2_score,'-',p1_score)
            else:
                print('it was a draw',self.p1.name(),p1_score,self.p2.name(),p2_score)
        
        return p1_score, p2_score
    
    # Function to plot circles
    def add_circle(self, ax, color, x, y):
        circle = plt.Circle((x, y), 0.1, color=color)
        ax.add_artist(circle)

    def visualize_result(self, visualize, p1_history, p2_history):
        if visualize == False:
            return
        
        # Initialize figure and axes for two rows
        fig, axs = plt.subplots(2, 1, figsize=(5, 5))
        plt.xlim(0, self.rounds)
        plt.ylim(0, 1)

        # Iteratively add circles to two rows
        for round in range(self.rounds):
            if p1_history[round] == 'C':
                c1 = 'green'
            else:
                c1 = 'red'
            
            if p2_history[round] == 'C':
                c2 = 'green'
            else:
                c2 = 'red'

            # Add red circle in the first row
            self.add_circle(axs[0], c1, round, 0.5)
            
            # Add green circle in the second row
            self.add_circle(axs[1], c2, round, 0.5)

        # Set limits and aspect ratio
        for ax in axs:
            ax.set_xlim(0, self.rounds)
            ax.set_ylim(0, 1)
            ax.set_aspect('equal')

        plt.show()

def main(args=None):
    payoff_mat = PayOffMatrix().return_payoff()
    game = Game(player1=TitForTat, player2=BetterAndBetter, payoff=payoff_mat, rounds=20, visualize=True, noise = 0.1)
    game.play()

if __name__ == '__main__':
    main()