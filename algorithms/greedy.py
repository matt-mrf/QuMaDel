from algorithms.helpers import diff, apply_color, get_costs
import random
import pprint


class Greedy:

    """
    Uses an pre made graph, and optimises it by changing
    the color of the neighbours and checking the result
    """

    def __init__(self, input, costscheme):
        self.input = input
        self.all_colors = [1, 2, 3, 4, 5, 6, 7]
        self.costscheme = costscheme

    def greedy_fill(self):
        gc = self.input.check_graph()
        while not self.input.found():
            for counter, node in enumerate(self.input.wrong_nodes):
                neighbour_colors = []
                for neighbour in node.neighbours:
                    neighbour_colors.append(neighbour.color)

                leftover_colors = diff(self.all_colors, neighbour_colors)
                if leftover_colors != []:
                    new_color = apply_color(leftover_colors)
                    gc[1][counter].color = new_color

            gc = self.input.check_graph()

        cost = get_costs(self.input, self.costscheme)
        return [self.input, cost]

# find wrong node
# find color of neighborig nodes
# remove these colours from possible_colors(list)
# apply left over color to nodes

# check again


# Pseudocode
# Wat krijg je binnen (nodes, counter)
#
# en dan een van de buren met dezelfde kleur aanpassen,
# checken hoeveel buren dezelfde kleur hebben
# counters met elkaar vergelijken, en dan doorgaan.
# List diff, eerste lijst is lijst van kleuren
# tweede lijst is afhankelijk van de kleuren van de buren. Die haal je van de eerste lijst af.
# Deze kleur ken die node aan

# pseudo hc_counter:
# check random graph
# sla counter op
# vervang eerste nodes kleur met beschikbare kleur
# haal kleur uit beschikbare kleuren
# check graph
# is nieuwe counter beter dan vorige?
# if ja:
#     opnieuw met betere graph
# else:
#     probeer volgende kleuren
#     if kleuren zijn op:
#         ga naar volgende node in wrong_nodes


# pseudo costs:
