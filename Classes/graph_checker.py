from graph import Graph

class graph_checker:

    def __init__(self, input):
        self.input = input
        self.amount_of_countries = len(input.nodes)
        self.neighbour_colors = []


    def check_graph(self):
        # graph object is input
        counter = 0
        for key, node in self.input.nodes.items():
            node_color = node.color
            self.neighbour_colors = []
            for neighbour in node.neighbours:
                self.neighbour_colors.append(neighbour.color)

            if node.color in self.neighbour_colors:
                counter += 1


        # print(f"amount of countries: {self.amount_of_countries}")
        # print(f"amount of countries not right: {counter}")
        pct = float(counter / self.amount_of_countries * 100)
        # print(f"percentage wrong: {pct}%")

        if pct == 0:
            print(self.neighbour_colors)
            self.neighbour_colors = ["found"]
            print(self.input.nodes)


    def found(self):
        if self.neighbour_colors == ["found"]:
            return True
        else:
            return False
