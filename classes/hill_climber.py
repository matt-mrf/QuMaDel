class hill_climber:

    """
    Uses an already made graph, and optimalises it by changing
    the color of the neighbours and checking the result
    """
    possible_colors = [1, 2, 3, 4, 5, 6, 7]

    def __init__(self, input):
        self.input = input


    def hillclimber (self):
        gc = self.input.check_graph()
        print(gc[1])
        neighbour_colors = []
        # while not self.input.found() == True:
        for node in self.input.wrong_nodes:
            pass








# Pseudocode
# Wat krijg je binnen (nodes, counter)
#
# en dan een van de buren met dezelfde kleur aanpassen,
# checken hoeveel buren dezelfde kleur hebben
# counters met elkaar vergelijken, en dan doorgaan.
# List diff, eerste lijst is lijst van kleuren
# tweede lijst is afhankelijk van de kleuren van de buren. Die haal je van de eerste lijst af.
# Deze kleur ken die node aan
