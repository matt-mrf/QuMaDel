import random
import copy


class Kempe:
    """
    Kempe's algorithm to k-color a graph
    """

    def __init__(self, amount):
        """
        Takes an empty graph to color
        """
        self.amount = amount
        self.all_colors = list(range(1, amount))

    def execute_kempe(self, in_graph):
        """
        Take empty Graph
        save for later coloring
        copy for extracting nodes
        k = number of desired colors - 1
        ---
        if there are nodes with degree < k:
            find node with degree < k
            remove it and update graph
            put removed node in stack
        else:
            pick arbitrary node, remove and put on stack

        color nodes in stack order in saved graph
            find color for node that isnt already used in adjecent node
            if no such color exists, keep empty and save node
        """
        # save graph for later coloring
        out_graph = in_graph
        cur_graph = in_graph
        k = self.amount - 1  # number of colors to initially use
        stack = []
        while not out_graph.found():
            out_graph = copy.deepcopy(in_graph)
            cur_graph = copy.deepcopy(in_graph)
            # do for length of amount of nodes
            for i in range(len(cur_graph.nodes)):
                # pp.pprint(cur_graph.nodes)
                nodes = cur_graph.nodes
                # find node with degree less than k
                cur_node = None  # node to be deleted later
                for key, node in nodes.items():
                    degree = len(node.neighbours)
                    if degree < k:  # find node with degree < k
                        cur_node = node
                        break
                if cur_node is None:  # if there are no nodes with degree < k
                    # pick node with lowest degree
                    cur_node = random.choice(list(nodes.values()))

                # remove node from working graph and put on stack
                cur_graph.delete_node(cur_node.name)
                stack.append(cur_node.name)

            # color nodes in stack order
            uncolored_nodes = []
            for i in range(len(stack)):
                next_node = stack.pop()
                node_to_color = out_graph.nodes[next_node]

                neighbour_colors = []
                for neighbour in node_to_color.neighbours:
                    neighbour_colors.append(neighbour.color)
                # print(f"neighbour_colors {neighbour_colors}")

                # print(f"node to color: {node_to_color}")
                # for neighbour in node_to_color.neighbours:
                    # print(f"neighbour: {neighbour}")

                leftover_colors = self.diff(self.all_colors, neighbour_colors)
                # print(leftover_colors)
                if leftover_colors == []:  # if there are no colors left to give
                    # save node to color later
                    uncolored_nodes.append(node_to_color)
                else:
                    new_color = self.apply_color(leftover_colors)
                    # print(new_color)
                    node_to_color.color = new_color

            for node in uncolored_nodes:
                node.color = self.amount

            gc = out_graph.check_graph()
        return out_graph

    def diff(self, first, second):
        second = set(second)
        return [item for item in first if item not in second]

    def apply_color(self, leftover_colors):
        """
        Applies a random color from given leftover colors.
        """
        color = random.choice(leftover_colors)
        return color
