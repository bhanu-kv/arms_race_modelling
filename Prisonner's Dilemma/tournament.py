# from match import Game
# from strategies import *
# from payoffs import PayOffMatrix
# import glob
# import importlib
# import inspect
# import os
# import collections

# class Tournament():
#     def __init__(self, games, players, rounds, noise):
#         self.players = players
#         self.scores = {}
#         self.rounds = rounds
#         self.noise = noise
#         self.games = games

#         for player in self.players:
#             self.scores[player.name] = 0
    
#     def play(self):
#         for game in range(self.games):
#             for i in range(len(self.players)):
#                 for j in range(i, len(self.players)):
#                     if i != j:
#                         payoff_mat = PayOffMatrix().return_payoff()
#                         game = Game(player1=self.players[i], player2=self.players[j], payoff=payoff_mat, rounds=self.rounds, visualize=False, noise = self.noise)
#                         s1, s2 = game.play()
#                         # print(f"{self.players[i].name}: {s1} vs {self.players[j].name}: {s2}")
#                         self.scores[self.players[i].name] += s1
#                         self.scores[self.players[j].name] += s2
    
#     def show_result(self):
#         counter = collections.Counter(self.players)
        
#         for player in counter:
#             self.scores[player.name] /= (counter[player])
#             self.scores[player.name] /= self.rounds
#             self.scores[player.name] /= self.games
        
#         print(dict(sorted(self.scores.items(), key=lambda item: item[1], reverse=True)))

# def main(args=None):
#     strategies = []
#     repeat_strats = 5

#     current_dir = os.path.join(os.path.dirname(os.path.abspath('./strategies/*.py')))
#     current_module_name = os.path.splitext(os.path.basename(current_dir))[0]
#     for file in glob.glob(current_dir + "/*.py"):
#         name = os.path.splitext(os.path.basename(file))[0]

#         # Ignore __ files
#         if name.startswith("__"):
#             continue

#         module = importlib.import_module("." + name,package=current_module_name)

#         for member in dir(module):
#             handler_class = getattr(module, member)

#             if handler_class and inspect.isclass(handler_class):
#                 strategy_member = handler_class()

#                 for i in range(repeat_strats):
#                     strategies.append(strategy_member)
    
#     tournament = Tournament(games = 5, players = strategies, rounds = 200, noise = 0.001)
#     tournament.play()
#     tournament.show_result()

# if __name__ == '__main__':
#     main()

##############################################################################################################################################
# import glob
# import importlib
# import inspect
# import os
# import collections
# import random
# from match import Game
# from strategies import *  # Assuming you have a strategies.py file
# from payoffs import PayOffMatrix

# class EvolutionaryTournament:
#     def __init__(self, games, rounds, noise, population_size, generations):
#         self.population_size = population_size
#         self.generations = generations
#         self.rounds = rounds
#         self.games = games
#         self.noise = noise
#         self.strategies = self.initialize_population()
        
#     def initialize_population(self):
#         strategies = []
#         repeat_strats = 5
#         current_dir = os.path.dirname(os.path.abspath(__file__)) + "/strategies"
        
#         for file in glob.glob(os.path.join(current_dir, "*.py")):
#             name = os.path.splitext(os.path.basename(file))[0]
#             if name.startswith("__"):
#                 continue
#             module = importlib.import_module(f"strategies.{name}")
#             for member in dir(module):
#                 handler_class = getattr(module, member)
#                 if inspect.isclass(handler_class):
#                     strategy_instance = handler_class()
#                     for _ in range(repeat_strats):
#                         strategies.append(strategy_instance)
        
#         return strategies  # Initialize with a set of strategies

#     def play(self):
#         for generation in range(self.generations):
#             scores = {player.name: 0 for player in self.strategies}
            
#             for game in range(self.games):
#                 for i in range(len(self.strategies)):
#                     for j in range(i + 1, len(self.strategies)):
#                         payoff_mat = PayOffMatrix().return_payoff()
#                         game = Game(
#                             player1=self.strategies[i],
#                             player2=self.strategies[j],
#                             payoff=payoff_mat,
#                             rounds=self.rounds,
#                             visualize=False,
#                             noise=self.noise
#                         )
#                         s1, s2 = game.play()
#                         scores[self.strategies[i].name] += s1
#                         scores[self.strategies[j].name] += s2
            
#             self.evolve(scores)

#     def evolve(self, scores):
#         # Sort strategies based on their scores
#         sorted_strategies = sorted(scores.items(), key=lambda item: item[1], reverse=True)
        
#         # Select top-performing strategies
#         selected = [self.strategies[int(i * len(self.strategies) / 10)] for i in range(5)]  # Top 10%
        
#         # Generate new population
#         new_population = []
#         while len(new_population) < self.population_size:
#             parent1 = random.choice(selected)
#             parent2 = random.choice(selected)
#             child = self.reproduce(parent1, parent2)
#             new_population.append(child)
        
#         self.strategies = new_population  # Replace old population with new one

#     def reproduce(self, parent1, parent2):
#         # Simple crossover - mixing two strategies (modify as per your strategy structure)
#         child = parent1.__class__()  # Create a new instance of parent1's class
#         # For mutation, you can add logic here to tweak child's strategy
#         return child
    
#     def show_result(self):
#         final_scores = {player.name: 0 for player in self.strategies}
#         for player in self.strategies:
#             final_scores[player.name] = player.name  # Just for display, adjust as needed
#         print(dict(sorted(final_scores.items(), key=lambda item: item[1], reverse=True)))

# def main(args=None):
#     tournament = EvolutionaryTournament(games=5, rounds=200, noise=0.001, population_size=20, generations=10)
#     tournament.play()
#     tournament.show_result()

# if __name__ == '__main__':
#     main()

#####################################################################################################################################

import glob
import importlib
import inspect
import os
import collections
import random
from match import Game
from strategies import *  # Assuming you have a strategies.py file
from payoffs import PayOffMatrix

class EvolutionaryTournament:
    def __init__(self, games, rounds, noise, generations, mutation):
        self.generations = generations
        self.rounds = rounds
        self.noise = noise
        self.games = games
        self.mutation_probab = mutation
        self.strategies = self.initialize_population()

        self.scores = {}
        self.object_scores = {}

        self.score_history = []
        self.population_history = []
        
    def initialize_population(self):
        strategies = []
        repeat_strats = 5
        current_dir = os.path.dirname(os.path.abspath(__file__)) + "/strategies"
        
        for file in glob.glob(os.path.join(current_dir, "*.py")):
            name = os.path.splitext(os.path.basename(file))[0]
            if name.startswith("__"):
                continue
            module = importlib.import_module(f"strategies.{name}")
            for member in dir(module):
                handler_class = getattr(module, member)
                if inspect.isclass(handler_class):
                    strategy_instance = handler_class()
                    strategies.extend([strategy_instance] * repeat_strats)
        
        # random.shuffle(strategies)  # Randomize initial population
        # return strategies[:self.initial_population]  # Limit to the initial population size
        return strategies

    def play(self):
        for generation in range(self.generations):
            scores = {player.name: 0 for player in self.strategies}
            object_scores = {player: 0 for player in self.strategies}
            
            # Play all pairs of strategies
            for game in range(self.games):
                for i in range(len(self.strategies)):
                    for j in range(i + 1, len(self.strategies)):
                        payoff_mat = PayOffMatrix().return_payoff()
                        game = Game(
                            player1=self.strategies[i],
                            player2=self.strategies[j],
                            payoff=payoff_mat,
                            rounds=self.rounds,
                            visualize=False,
                            noise=self.noise
                        )
                        s1, s2 = game.play()
                        scores[self.strategies[i].name] += s1
                        object_scores[self.strategies[i]] += s1

                        scores[self.strategies[j].name] += s2
                        object_scores[self.strategies[j]] += s2
            
            print("Generation: ", generation)
            print(dict(sorted(scores.items(), key=lambda item: item[1], reverse=True)))

            self.evolve(scores)
            
            self.scores = scores
            self.object_scores = object_scores

            self.score_history.append(self.scores)

    def evolve(self, scores):
        # Create a new frequency dictionary based on scores
        frequency = {player.name: 0 for player in self.strategies}
        total_score = sum(scores.values())

        for player in self.strategies:
            if total_score > 0:  # Avoid division by zero
                frequency[player.name] = max(1, int(scores[player.name] / total_score * 100))  # Scale frequencies
        
        # Rebuild the population based on frequency
        new_population = []
        for name, freq in frequency.items():
            strategy = next(s for s in self.strategies if s.name == name)
            new_population.extend([strategy] * freq)  # Add strategy based on frequency

        # Randomly mutate the population
        self.strategies = new_population
        self.population_history.append(new_population)
        self.mutate_population()

    def mutate_population(self):
        for i in range(len(self.strategies)):
            if random.random() < self.mutation_probab:
                # Replace this strategy with a random new one from the full pool of strategies
                new_strategy = random.choice(self.strategies)
                self.strategies[i] = new_strategy  # Mutate (replace) the strategy

    def show_result(self):
        # final_scores = {player.name: 0 for player in self.strategies}
        # for player in self.strategies:
        #     final_scores[player.name] = player.name  # Just for display, adjust as needed
        # print(dict(sorted(final_scores.items(), key=lambda item: item[1], reverse=True)))
        pass

def main(args=None):
    tournament = EvolutionaryTournament(games=5, rounds=200, noise=0.005, generations=50, mutation=0.001)
    tournament.play()
    tournament.show_result()

if __name__ == '__main__':
    main()
