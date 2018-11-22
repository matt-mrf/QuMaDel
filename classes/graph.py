from classes.node import Node


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
        self.counter = 0
        self.neighbour_colors = []
        self.wrong_nodes = []

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


    def check_graph(self):
        self.counter = 0
        self.wrong_nodes = []
        # check each node
        for key, node in self.nodes.items():
            node_color = node.color
            self.neighbour_colors = []
            # add neighbours' colors to neighbours list of node
            for neighbour in node.neighbours:
                self.neighbour_colors.append(neighbour.color)

            if node.color in self.neighbour_colors:
                self.counter += 1
                self.wrong_nodes.append(node)




        # print(f"amount of countries: {self.amount_of_countries}")
        # print(f"amount of countries not right: {counter}")
        # pct = float(counter / self.amount_of_countries * 100)
        # print(f"percentage wrong: {pct}%")

        # check to see if graph has nodes without conflicting
        # neighbouring nodes
        if self.counter == 0:
            # output found graph per node
            self.neighbour_colors = ["found"]
            return []
        else:
            return [self.counter, [self.wrong_nodes]]
            print(wrong_nodes)


    def found(self):
        """
        checks to see if graph is a valid graph
        """
        if self.neighbour_colors == ["found"]:
            return True
        else:
            return False


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
