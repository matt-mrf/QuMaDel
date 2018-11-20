# from graph import Graph

class graph_checker:

    def __init__(self, input):
        # initialize values
        self.input = input
        self.amount_of_countries = len(input.nodes)
        self.neighbour_colors = []


    def check_graph(self):
        counter = 0
        # check each node
        for key, node in self.input.nodes.items():
            node_color = node.color
            self.neighbour_colors = []
            # add neighbours' colors to neighbours list of node
            for neighbour in node.neighbours:
                self.neighbour_colors.append(neighbour.color)

            if node.color in self.neighbour_colors:
                counter += 1


        # print(f"amount of countries: {self.amount_of_countries}")
        # print(f"amount of countries not right: {counter}")
        # pct = float(counter / self.amount_of_countries * 100)
        # print(f"percentage wrong: {pct}%")

        # check to see if graph has nodes without conflicting
        # neighbouring nodes
        if counter == 0:
            self.neighbour_colors = ["found"]
            # output found graph per node
            print(self.input.nodes)


    def found(self):
        """
        checks to see if graph is a valid graph
        """
        if self.neighbour_colors == ["found"]:
            return True
        else:
            return False
