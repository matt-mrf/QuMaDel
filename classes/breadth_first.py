class breadth_first.py:

    def init(self, costscheme):
        self.costscheme = costscheme

def depth_first(state, colored_nodes, depth, max_depth, in_graph, costscheme):
    lowestscore = None

    # solution found, determine map score
    if len(colored_nodes) == len(country.nodes):
        resultscore = lowestScoreDepthFirst(coloredRegions, costscheme)

        # keep track of the lowest score
        if resultscore < lowestscore:
            lowestscore = resultscore
            for key, value in coloredRegions.items():
                country.regions[key].transmitter = value
            drawGraph(country.regions, config.country + str(lowestscore))
            print('Lowestscore is now: ' + str(lowestscore))

    # base case, continue until max depth reached
    if depth < maxDepth:

        # symmetrical pruning, once the first region changes of color, quit.
        # try:
        #     if coloredRegions[0] != 'red':
        #         exit()
        # except KeyError:
        #     pass

        # colors we can use, avoids adjacent neighbours with the same color
        availableColors = [color for color in config.colors if color not in
                           [val for key, val in coloredRegions.items()
                            if key in country.regions[depth].neighbours]]

        # for each available color, generate all possible combinations
        for color in availableColors:
            state.append(color)
            coloredRegions[depth] = color
            colorMapDepthFirst(state, depth + 1, maxDepth,
                               coloredRegions, country, costscheme)
            state.pop()
            coloredRegions.pop(depth, None)
