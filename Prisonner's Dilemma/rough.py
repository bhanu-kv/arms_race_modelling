# def evolve_2(self, scores):
#     # Create a new frequency dictionary based on scores
#     frequency = {player.name: 0 for player in self.list_strats}
#     total_score = sum(scores.values())

#     counter = collections.Counter(self.strategies)

#     for player in self.list_strats:
#         if total_score > 0:  # Avoid division by zero
#             frequency[player.name] = (1+(scores[player.name]/total_score)-0.04)*counter[player] # Scale frequencies
#             # frequency[player.name] = (1+(scores[player.name]/total_score)-(counter[player]/len(self.strategies)))*counter[player] # Scale frequencies
    
#     # Rebuild the population based on frequency
#     new_population = []
#     for name, freq in frequency.items():
#         strategy = next(s for s in self.list_strats if s.name == name)
#         new_population.extend([strategy] * int(freq))  # Add strategy based on frequency

#     # Randomly mutate the population
#     self.strategies = new_population
#     self.mutate_population()