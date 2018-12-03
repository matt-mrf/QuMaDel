class Depth:

    def __init__(self, costscheme, amount):
        self.costscheme = costscheme
        self.all_colors = list(range(1, amount))

    def depth_first(self, state, colored_nodes, depth, max_depth, in_graph):
        lowestscore = None

        # # solution found, determine map score
        # if len(colored_nodes) == len(in_graph.nodes):
        #     score = get_costs(in_graph)
        #
        #     # keep track of the lowest score
        #     if resultscore < lowestscore:
        #         lowestscore = resultscore
        #         for key, value in coloredRegions.items():
        #             country.regions[key].transmitter = value
        #         drawGraph(country.regions, config.country + str(lowestscore))
        #         print('Lowestscore is now: ' + str(lowestscore))

        # continue until max depth reached
        if depth < max_depth:
            next_node = list(in_graph.nodes)[depth]
            cur_node = in_graph.nodes[next_node]
            print(cur_node)

            # find available colors for next node
            neighbour_colors = []
            for neighbour in cur_node.neighbours:
                neighbour_colors.append(neighbour.color)

            leftover_colors = self.diff(self.all_colors, neighbour_colors)
            print(f"leftover: {leftover_colors}")

            # for each available color, generate all possible combinations
            for color in leftover_colors:
                state.append(color)
                print(state)
                colored_nodes[depth] = color
                self.depth_first(state, colored_nodes, depth + 1, max_depth,
                                 in_graph)
                state.pop()
                colored_nodes.pop(depth, None)

    def get_costs(self, graph):
        total_costs = 0
        for key, node in graph.nodes.items():
            color = node.color
            total_costs += self.costscheme[color]
        return total_costs

    def diff(self, first, second):
        second = set(second)
        return [item for item in first if item not in second]
