from algorithms.helpers import diff, apply_color, get_costs
import random
import pprint


class Greedy:

    def __init__(self, input, costscheme):
        """
        An initializer takes a randomly generated input graph and costcheme
        """"
        self.input = input
        self.all_colors = [1, 2, 3, 4, 5, 6, 7]
        self.costscheme = costscheme

    def greedy_fill(self):
        """
        Uses an pre made graph, and optimises it by changing
        the color of the neighbours and checking the result
        """

        # check graph with given input
        gc = self.input.check_graph()

        # continue untill valid graph is found
        while not self.input.found():
            # iterate through wrong color nodes
            for counter, node in enumerate(self.input.wrong_nodes):

                # make list of neighbouring colors of node
                neighbour_colors = []
                for neighbour in node.neighbours:
                    neighbour_colors.append(neighbour.color)

                # make list of leftover colors
                leftover_colors = diff(self.all_colors, neighbour_colors)

                if leftover_colors != []:
                    #apply new color to node
                    new_color = apply_color(leftover_colors)
                    gc[1][counter].color = new_color

            # check graph
            gc = self.input.check_graph()

        # return cost and coloured graph
        cost = get_costs(self.input, self.costscheme)
        return [self.input, cost]
