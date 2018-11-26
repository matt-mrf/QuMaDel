class Node:
    """
    Node class, representing a province within a country.
    Contains information about itself and neighbouring
    countries.
    """

    def __init__(self, name, neighbours):
        """
        initialize object by giving it a dictonary representing the
        adjecency list
        """

        self.name = name
        self.color = 0
        self.neighbours = neighbours

    def set_color(self, given_color):
        """
        sets the color of a node
        """
        self.color = given_color

    def __repr__(self):
        return f"Name: {self.name}, Color: {self.color}"
