class Node:
    """
    Node class, representing a province within a country.
    Contains information about itself and neighbouring
    countries.
    """

    def __init__(self, name, color, neighbours):
        """
        initialize object by giving it a dictonary representing the
        adjecency list
        """

        self.name = name
        self.color = color
        self.neighbours = neighbours


    def set_color(self, given_color):
        """
        sets the color of a node
        """
        self.color = given_color


if __name__ == "__main__":
    node1 = Node("noord", "none", ["west", "oost"])
    node2 = Node("west", "none", ["zuid", "noord"])
    node3 = Node("oost", "none", ["noord", "zuid"])

    node3.set_color("rood")
    node1.set_color("geel")

    print(node1.color)
    print(node3.color)
    print("hallo")
