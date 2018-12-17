from algorithms.helpers import diff, calc_probability, get_costs
import random
import copy


class Hill_climber:

    def __init__(self, costscheme):
        """
        takes a cost scheme as input
        """
        self.costscheme = costscheme

    def hill_climber(self, in_graph):
        """
        hill climbing algotithm. Changes a graph incrementally
        and checks for improvement in cost. If no improvement
        happens, the change will be rejected.
        """
        iterations = 5000

        cost_list = []
        cost = 0

        for i in range(iterations):
            # calculate initial costs
            initial_costs = get_costs(in_graph, self.costscheme)
            cost = initial_costs
            cost_list.append(cost)

            found = False
            while not found:
                # find random node in graph
                rand_int = random.choice(list(in_graph.nodes.keys()))
                cur_node = in_graph.nodes[rand_int]

                # create list of neighbouring colors of current node
                neighbour_colors = []
                for neighbour in cur_node.neighbours:
                    neighbour_colors.append(neighbour.color)

                # get list of available colors
                available_colors = diff(
                    list(range(1, len(self.costscheme) + 1)), neighbour_colors)

                # if more than one available color exists
                if len(available_colors) > 1:
                    found = True

                    # save original color for later
                    original_color = cur_node.color

                # remove original color from available list to avoid
                # changing to the same color
                available_colors.remove(original_color)

                # apply new color to node
                new_color = random.choice(available_colors)
                cur_node.color = new_color

            # calculate costs of new graph
            new_costs = get_costs(in_graph, self.costscheme)

            # do not accept change if cost is higher than before
            if new_costs > initial_costs:
                cur_node.color = original_color

        lowest_cost = cost_list[-1]
        return [in_graph, cost_list, lowest_cost]

    def hill_climber_n_opt(self, in_graph, n):

        iterations = 10000

        cost_list = []
        for i in range(iterations):

            # calculate initial costs
            initial_costs = get_costs(in_graph, self.costscheme)
            cost = initial_costs
            cost_list.append(cost)

            checked_nodes = {}

            # find n nodes
            for j in range(n):
                found = False
                while not found:

                    # find nodes that are able to be changed, needs to be n
                    # different ones
                    while True:
                        rand_int = random.choice(list(in_graph.nodes.keys()))
                        cur_node = in_graph.nodes[rand_int]
                        if cur_node.name not in checked_nodes:
                            break

                    # make list of neighbouring nodes
                    neighbour_colors = []
                    for neighbour in cur_node.neighbours:
                        neighbour_colors.append(neighbour.color)

                    # determine available colors for node
                    available_colors = diff(
                        list(range(1, len(self.costscheme) + 1)), neighbour_colors)

                    if len(available_colors) > 1:
                        found = True
                        # add node to checked nodes and save original color
                        checked_nodes[cur_node.name] = cur_node.color
                        original_color = cur_node.color

                        available_colors.remove(original_color)

                        # find new color for node
                        new_color = random.choice(available_colors)
                        cur_node.color = new_color

            # calculate new cost
            new_costs = get_costs(in_graph, self.costscheme)

            # if new costs are higher than before, dont accept change
            if new_costs > initial_costs:
                for name, color in checked_nodes.items():
                    in_graph.nodes[name].color = color

        lowest_cost = cost_list[-1]
        return [in_graph, cost_list, lowest_cost]

    def hill_climber_annealing(self, in_graph):

        # initial values
        tMax = 30000
        temp = tMax
        tMin = 0.1
        cooling = 0.0001

        cost_list = []

        # calculate initial cost
        initial_costs = get_costs(in_graph, self.costscheme)

        cost = initial_costs

        while temp > tMin:
            cost_list.append(cost)

            found = False
            while not found:

                # choose random node to change color of
                rand_int = random.choice(list(in_graph.nodes.keys()))
                cur_node = in_graph.nodes[rand_int]


                # create list of neighbouring colors of current node
                neighbour_colors = []
                for neighbour in cur_node.neighbours:
                    neighbour_colors.append(neighbour.color)

                # get list of available colors
                available_colors = diff(
                    list(range(1, len(self.costscheme) + 1)), neighbour_colors)

                # if more than one available color exists
                if len(available_colors) > 1:
                    found = True

                    # save original color for later
                    original_color = cur_node.color

                    # remove original color from available list to avoid
                    # changing to the same color
                    available_colors.remove(original_color)

                    # apply new color to node
                    new_color = random.choice(available_colors)
                    cur_node.color = new_color

            # calculate costs of new graph
            new_costs = get_costs(in_graph, self.costscheme)

            # calculate the probability of change being accepted
            if calc_probability(cost, new_costs, temp) > random.random():
                cost = new_costs
            else:
                # revert back to previous graph if not accepted
                cur_node.color = original_color

            # cool down the temperature so acceptance rate declines
            temp *= 1-cooling

        lowest_cost = cost_list[-1]
        return [in_graph, cost_list, lowest_cost]
