class Node:
    """
    Node class, representing a province within a country.
    Contains information about itself and neighbouring
    countries.
    """

    def __init__(self, name):
        """
        initialize object by giving it a dictonary representing the
        adjecency list
        """

        self.name = name
        self.color = "0"
        self.neighbours = []


    def set_color(self, given_color):
        """
        sets the color of a node
        """
        self.color = given_color


    def add_neighbour(self, Node):
        pass


    def __repr__(self):
        return f"Name: {self.name}, Color: {self.color}, Neighbours: {self.neighbours}"

if __name__ == "__main__":
    node1 = Node("noord", "none", ["west", "oost"])
    node2 = Node("west", "none", ["zuid", "noord"])
    node3 = Node("oost", "none", ["noord", "zuid"])

    node3.set_color("rood")
    node1.set_color("geel")

    print(node1.color)
    print(node3.color)
    print("hallo")
