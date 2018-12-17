from algorithms.helpers import diff, get_costs
import random
import copy

class Randomizer:

    def randomize_graph(self, in_graph, amount):
        """
        """
        random.seed()
        removed_graph = copy.deepcopy(in_graph)
        all_colors = list(range(1, amount))

        # do until every node is colored
        while removed_graph.nodes != {}:

            # choose random node to assign a color to
            rand_int = random.choice(list(removed_graph.nodes.keys()))
            random_node = in_graph.nodes[str(rand_int)]

            neighbour_colors = []
            for neighbour in random_node.neighbours:
                neighbour_colors.append(neighbour.color)

            # find available colors
            available_colors = diff(all_colors, neighbour_colors)

            if available_colors == []:
                return False
            else:
                random_color = random.choice(available_colors)
                random_node.color = random_color

            # remove country from object to track progress
            removed_graph.nodes.pop(str(rand_int))

        return in_graph
