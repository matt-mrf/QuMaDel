from datastructure.node import Node


class Graph:
    """
    Graph class, representing a country with provinces or states
    """

    costs1 = {1: 12, 2: 26, 3: 27, 4: 30, 5: 37, 6: 39, 7: 41}
    # costs2 = {1: 19, 2: 20, 3: 21, 4: 23, 5: 36, 6: 37, 7: 38}
    # costs3 = {1: 16, 2: 17, 3: 31, 4: 33, 5: 36, 6: 56, 7: 57}
    # costs4 = {1: 3, 2: 34, 3: 36, 4: 39, 5: 41, 6: 43, 7: 58}

    def __init__(self, graph_dict):
        """
        initialize object by giving it a dictonary representing the
        adjecency list
        """
        self.original_graph = graph_dict
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

    def delete_node(self, node_name):
        """
        Deletes specified node from a graph
        """
        # delete node from neighbouring nodes
        del_node = self.nodes[node_name]
        for neighbour in del_node.neighbours:
            neighbour.neighbours.remove(del_node)

        # delete node itself
        del self.nodes[node_name]

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

            if node_color in self.neighbour_colors:
                self.counter += 1
                self.wrong_nodes.append(node)

        # check to see if graph has nodes without conflicting
        # neighbouring nodes
        if self.counter == 0:
            # output found graph per node
            self.neighbour_colors = ["found"]
            return []
        else:
            return [self.counter, self.wrong_nodes]
            print(self.wrong_nodes)

    def found(self):
        """
        checks to see if graph is a valid graph
        """
        if self.neighbour_colors == ["found"]:
            return True
        else:
            return False

    def costs(self):
        total = 0
        for key, node in self.nodes.items():
            total += self.costs1[node.color]

        return total


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
    print(graph_ukraine.nodes)
