import random

class Randomizer:

    def randomize_graph(self, in_graph):

        for key, node in in_graph.nodes.items():
            color = random.randint(1, 4)
            node.set_color(color)

        return in_graph


if __name__ == "__main__":
    passS
