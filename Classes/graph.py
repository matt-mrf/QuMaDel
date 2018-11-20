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
        self.nodes = {}

    def create_graph(self):
        """
        creates nodes and connects them in the graph
        """
        # create all node objects
        for node in self.graph:
            node_obj = Node(node, self.graph[node])
            # add node object with name as index
            self.nodes[node] = node_obj

        # replace neighbour names with objects
        for node in self.nodes:
            obj = self.nodes[node]
            # copy names of neighbours to temp list
            n_list = obj.neighbours
            obj.neighbours = []
            # go over letters in neighbours
            for neighbour in n_list:
                # find the corresponding object
                neighbour_obj = self.nodes[neighbour]
                obj.neighbours.append(neighbour_obj)


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
    graph_ukraine.create_graph()
