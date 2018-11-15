from node import Node

class Graph:
    """
    Graph class, representing a country with provinces or states
    """

    def __init__(self, graph_dict):
        """
        initialize object by giving it a dictonary representing the
        adjecency list
        """
        self.graph = graph_dict
        self.nodes = []

    def add_nodes(self):
        """
        creates nodes and connects them in the graph
        """
        for node in self.graph:
            print(self.graph)


if __name__ == "__main__":
    ukraine = {'A': ['F', 'B'],
    'B': ['A', 'F', 'E', 'D', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'B', 'E', 'H'],
    'E': ['D', 'B', 'F', 'G', 'H'],
    'F': ['A', 'B', 'E', 'G', 'J'],
    'G': ['E', 'F', 'J', 'I', 'H'],
    'H': ['D', 'E', 'G', 'I'],
    'I': ['H', 'G', 'J', 'K', 'N', 'O', 'L'],
    'J': ['F', 'G', 'I', 'K'],
    'K': ['J', 'I', 'N', 'R', 'M'],
    'L': ['I', 'O', 'P'],
    'M': ['Q', 'K'],
    'N': ['K', 'R', 'O', 'I'],
    'O': ['I', 'N', 'R', 'U', 'P', 'L'],
    'P': ['L', 'O', 'U', 'S'],
    'Q': ['M', 'R'],
    'R': ['K', 'Q', 'W', 'U', 'O', 'N'],
    'S': ['P', 'U', 'V', 'T'],
    'T': ['S'],
    'U': ['R', 'W', 'X', 'V', 'S', 'P', 'O'],
    'V': ['S', 'U', 'X'],
    'W': ['R', 'U', 'X', 'Y'],
    'X': ['V', 'U', 'W', 'Y'],
    'Y': ['W', 'X']}

    graph_ukraine = Graph(ukraine)

    graph_ukraine.add_nodes()
