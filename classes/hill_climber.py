import random
import pprint

class hill_climber:

    """
    Uses an already made graph, and optimalises it by changing
    the color of the neighbours and checking the result
    """


    def __init__(self, input):
        self.input = input
        self.all_colors = [1, 2, 3, 4, 5, 6, 7]


    def diff(self, first, second):
        second = set(second)
        return [item for item in first if item not in second]


    def hillclimber (self):
        gc = self.input.check_graph()
        while not self.input.found():
            gc = self.input.check_graph()
            print(gc[0], gc[1])
            i = 0
            for node in self.input.wrong_nodes:
                neighbour_colors = []
                for neighbour in node.neighbours:
                    neighbour_colors.append(neighbour.color)

                leftover_colors = (self.diff(self.all_colors, neighbour_colors))
                if leftover_colors != []:
                    new_color = self.apply_color(leftover_colors)

                    gc[1][0][i].color = new_color
                    i += 1

        pp = pprint.PrettyPrinter()
        pp.pprint(self.input.nodes)


    def apply_color (self, leftover_colors):
        color = random.choice(leftover_colors)
        # print(f"new color {color}")
        return color







            # find wrong node
            # find color of neighborig nodes
            # remove these colours from possible_colors(list)
            # apply left over color to nodes

            #check again







# Pseudocode
# Wat krijg je binnen (nodes, counter)
#
# en dan een van de buren met dezelfde kleur aanpassen,
# checken hoeveel buren dezelfde kleur hebben
# counters met elkaar vergelijken, en dan doorgaan.
# List diff, eerste lijst is lijst van kleuren
# tweede lijst is afhankelijk van de kleuren van de buren. Die haal je van de eerste lijst af.
# Deze kleur ken die node aan
