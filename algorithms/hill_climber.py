from algorithms.helpers import diff, calc_probability, get_costs
import random
import copy


class Hill_climber:

    def __init__(self, costscheme):
        self.costscheme = costscheme

    def hill_climber(self, in_graph):
        iterations = 1000000

        cost_list = []
        cost = 0

        for i in range(iterations):

            initial_costs = get_costs(in_graph, self.costscheme)
            cost = initial_costs
            cost_list.append(cost)

            found = False
            while not found:
                rand_int = random.choice(list(in_graph.nodes.keys()))
                cur_node = in_graph.nodes[rand_int]

                neighbour_colors = []
                for neighbour in cur_node.neighbours:
                    neighbour_colors.append(neighbour.color)

                available_colors = diff(
                    list(range(1, len(self.costscheme) + 1)), neighbour_colors)

                if len(available_colors) > 1:
                    found = True

                    original_color = cur_node.color

                available_colors.remove(original_color)

                new_color = random.choice(available_colors)
                cur_node.color = new_color

            new_costs = get_costs(in_graph, self.costscheme)

            if new_costs > initial_costs:
                cur_node.color = original_color

        lowest_cost = cost_list[-1]
        return [in_graph, cost_list, lowest_cost]

    def hill_climber_n_opt(self, in_graph, n):

        iterations = 1000000

        cost_list = []
        for i in range(iterations):

            initial_costs = get_costs(in_graph, self.costscheme)
            cost = initial_costs
            cost_list.append(cost)

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

                    available_colors = diff(
                        list(range(1, len(self.costscheme) + 1)), neighbour_colors)

                    if len(available_colors) > 1:
                        found = True
                        checked_nodes[cur_node.name] = cur_node.color
                        original_color = cur_node.color

                        available_colors.remove(original_color)

                        new_color = random.choice(available_colors)
                        cur_node.color = new_color

            new_costs = get_costs(in_graph, self.costscheme)

            if new_costs > initial_costs:
                for name, color in checked_nodes.items():
                    in_graph.nodes[name].color = color

        lowest_cost = cost_list[-1]
        return [in_graph, cost_list, lowest_cost]

    def hill_climber_annealing(self, in_graph):

        tMax = 30000
        temp = tMax
        tMin = 0.1
        cooling = 0.0001

        cost_list = []

        initial_costs = get_costs(in_graph, self.costscheme)

        cost = initial_costs

        while temp > tMin:
            cost_list.append(cost)

            found = False
            while not found:
                rand_int = random.choice(list(in_graph.nodes.keys()))
                cur_node = in_graph.nodes[rand_int]

                neighbour_colors = []
                for neighbour in cur_node.neighbours:
                    neighbour_colors.append(neighbour.color)

                available_colors = diff(
                    list(range(1, len(self.costscheme) + 1)), neighbour_colors)

                if len(available_colors) > 1:
                    found = True

                    original_color = cur_node.color
                    available_colors.remove(original_color)

                    new_color = random.choice(available_colors)
                    cur_node.color = new_color

            new_costs = get_costs(in_graph, self.costscheme)

            if calc_probability(cost, new_costs, temp) > random.random():
                cost = new_costs
            else:
                # revert back to previous graph if not accepted
                cur_node.color = original_color

            temp *= 1-cooling

        lowest_cost = cost_list[-1]
        return [in_graph, cost_list, lowest_cost]
