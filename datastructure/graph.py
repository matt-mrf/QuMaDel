from datastructure.node import Node


class Graph:
    """
    Graph class, representing a country with provinces or states
    """

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
        """
        Checks to see if a graph is valid,
        meaning that there are no adjecent nodes with the same colorself.

        returns true if the graph is valid
        """
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
