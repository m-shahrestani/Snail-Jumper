import copy

import numpy as np

from player import Player


class Evolution:
    def __init__(self):
        self.game_mode = "Neuroevolution"

    def next_population_selection(self, players, num_players):
        """
        Gets list of previous and current players (μ + λ) and returns num_players number of players based on their
        fitness value.

        :param players: list of players in the previous generation
        :param num_players: number of players that we return
        """
        # TODO (Implement top-k algorithm here)
        # TODO (Additional: Implement roulette wheel here)
        # TODO (Additional: Implement SUS here)

        # TODO (Additional: Learning curve)

        fit_sum = 0
        fit_avg = 0
        fit_max = players[0].fitness
        fit_min = players[0].fitness
        for player in players:
            fit_sum += player.fitness
            if (player.fitness > fit_max):
                fit_max = player.fitness
            if (player.fitness < fit_min):
                fit_min = player.fitness
        fit_avg = fit_sum / len(players)
        line = str(fit_min) + " " + str(fit_max) + " " + str(fit_avg) + "\n"
        with open('curve_learning.txt', "a") as file:
            file.write(line)

        next_population = self.q_tournament(players, num_players)
        return next_population
        # return players[: num_players]

    def q_tournament(self, players, num_players):
        next_population = []
        q = 2
        for i in range(num_players):
            temp_population = []
            for j in range(q):
                temp_population.append(players[np.random.randint(0, len(players))])
            temp_population.sort(key=lambda x: x.fitness, reverse=True)
            next_population.append(temp_population[0])
        return next_population

    def generate_new_population(self, num_players, prev_players=None):
        """
        Gets survivors and returns a list containing num_players number of children.

        :param num_players: Length of returning list
        :param prev_players: List of survivors
        :return: A list of children
        """
        first_generation = prev_players is None
        if first_generation:
            return [Player(self.game_mode) for _ in range(num_players)]
        else:
            new_players = prev_players
            return new_players

    def clone_player(self, player):
        """
        Gets a player as an input and produces a clone of that player.
        """
        new_player = Player(self.game_mode)
        new_player.nn = copy.deepcopy(player.nn)
        new_player.fitness = player.fitness
        return new_player
