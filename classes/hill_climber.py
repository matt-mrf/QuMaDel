import random

class hill_climber:


    def __init__(self, costscheme):
        self.costscheme = costscheme

    def hill_climber(self, in_graph):

        cost = 0
        for i in range(100):

            initial_costs = self.get_costs(in_graph)
            cost = initial_costs

            found = False
            while not found:
                rand_int = random.choice(list(in_graph.nodes.keys()))
                cur_node = in_graph.nodes[rand_int]

                neighbour_colors = []
                for neighbour in cur_node.neighbours:
                    neighbour_colors.append(neighbour.color)



                available_colors = self.diff(list(range(1,len(self.costscheme)+1)), neighbour_colors)

                if len(available_colors) > 1:
                    found = True

                    original_color = cur_node.color

                available_colors.remove(original_color)

                new_color = random.choice(available_colors)
                cur_node.color = new_color

            new_costs = self.get_costs(in_graph)

            if new_costs > initial_costs:
                cur_node.color = original_color

        return cost


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
