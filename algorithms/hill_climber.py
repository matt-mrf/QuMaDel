import random
import copy
import math


class hill_climber:

    def __init__(self, costscheme):
        self.costscheme = costscheme

    def hill_climber(self, in_graph):

        cost = 0
        for i in range(1000):

            initial_costs = self.get_costs(in_graph)
            cost = initial_costs

            found = False
            while not found:
                rand_int = random.choice(list(in_graph.nodes.keys()))
                cur_node = in_graph.nodes[rand_int]

                neighbour_colors = []
                for neighbour in cur_node.neighbours:
                    neighbour_colors.append(neighbour.color)

                available_colors = self.diff(
                    list(range(1, len(self.costscheme) + 1)), neighbour_colors)

                if len(available_colors) > 1:
                    found = True

                    original_color = cur_node.color

                available_colors.remove(original_color)

                new_color = random.choice(available_colors)
                cur_node.color = new_color

            new_costs = self.get_costs(in_graph)

            if new_costs > initial_costs:
                cur_node.color = original_color
        print(cost)
        return cost

    def hill_climber_n_opt(self, in_graph, n):

        iterations = 3000
        cost = 0
        for i in range(iterations):

            initial_costs = self.get_costs(in_graph)
            cost = initial_costs

            checked_nodes = {}
            for j in range(n):
                found = False
                while not found:
                    while True:
                        rand_int = random.choice(list(in_graph.nodes.keys()))
                        cur_node = in_graph.nodes[rand_int]
                        if cur_node.name not in checked_nodes:
                            break

                    neighbour_colors = []
                    for neighbour in cur_node.neighbours:
                        neighbour_colors.append(neighbour.color)

                    available_colors = self.diff(
                        list(range(1, len(self.costscheme) + 1)), neighbour_colors)

                    if len(available_colors) > 1:
                        found = True
                        checked_nodes[cur_node.name] = cur_node.color
                        original_color = cur_node.color

                        available_colors.remove(original_color)

                        new_color = random.choice(available_colors)
                        cur_node.color = new_color

            new_costs = self.get_costs(in_graph)

            if new_costs > initial_costs:
                for name, color in checked_nodes.items():
                    in_graph.nodes[name].color = color

        return cost

    def hill_climber_annealing(self, in_graph):

        tMax = 100000
        temp = tMax
        tMin = 0.1
        cooling = 0.0001

        initial_costs = self.get_costs(in_graph)

        cost = initial_costs
        while temp > tMin:

            found = False
            while not found:
                rand_int = random.choice(list(in_graph.nodes.keys()))
                cur_node = in_graph.nodes[rand_int]

                neighbour_colors = []
                for neighbour in cur_node.neighbours:
                    neighbour_colors.append(neighbour.color)

                available_colors = self.diff(
                    list(range(1, len(self.costscheme) + 1)), neighbour_colors)

                if len(available_colors) > 1:
                    found = True

                    original_color = cur_node.color
                    available_colors.remove(original_color)

                    new_color = random.choice(available_colors)
                    cur_node.color = new_color

            new_costs = self.get_costs(in_graph)

            if self.calc_probability(cost, new_costs, temp) > random.random():
                cost = new_costs
            else:
                # revert back to previous graph if not accepted
                cur_node.color = original_color

            temp *= 1-cooling

                # # partly based on https://nl.wikipedia.org/wiki/Simulated_annealing
                # acceptance_prob = math.exp()
                # for name, color in checked_nodes.items():
                #     in_graph.nodes[name].color = color
        return cost

    def calc_probability(self, old_costs, new_costs, temp):
        if new_costs < old_costs:
            return 1.0
        else:
            return math.exp((old_costs - new_costs) / temp)

    def diff(self, first, second):
        second = set(second)
        return [item for item in first if item not in second]

    def get_costs(self, graph):
        total_costs = 0
        for key, node in graph.nodes.items():
            color = node.color
            # print(color)
            total_costs += self.costscheme[color]
        return total_costs
