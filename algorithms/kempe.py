from algorithms.helpers import diff, apply_color, get_costs
import random
import copy


class Kempe:
    """
    Kempe's algorithm to k-color a graph via finding nodes < k self,
    that will be put on a stack and be colored in via the stack order
    """

    def __init__(self, amount, costscheme):
        """
        Takes an empty graph to color
        """
        self.amount = amount
        self.all_colors = list(range(1, amount))
        self.costscheme = costscheme

    def execute_kempe(self, in_graph):

        # save graph for later coloring
        out_graph = in_graph
        cur_graph = in_graph

        # number of colors to initially use
        k = len(self.all_colors)
        stack = []
        while not out_graph.found():

        # for i in range(1):
            out_graph = copy.deepcopy(in_graph)
            cur_graph = copy.deepcopy(in_graph)

            # do for length of amount of nodes
            for i in range(len(cur_graph.nodes)):
                nodes = cur_graph.nodes

                # find node with degree less than k
                cur_node = None  # node to be deleted later
                i = 0
                for key, node in nodes.items():
                    degree = len(node.neighbours)

                    # find node with degree < k
                    if degree < k:
                        cur_node = node
                        break

                # if there are no nodes with degree < k
                if cur_node is None:

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

                # make list of neighbouring colors of node
                neighbour_colors = []
                for neighbour in node_to_color.neighbours:
                    neighbour_colors.append(neighbour.color)

                # make list of leftover possible colors
                leftover_colors = diff(self.all_colors, neighbour_colors)

                # if there ar no colors left to give
                if leftover_colors == []:

                    # save node to color later
                    uncolored_nodes.append(node_to_color)
                else:

                    # apply color to node from leftover color list
                    new_color = apply_color(leftover_colors)
                    node_to_color.color = new_color


            for node in uncolored_nodes:
                node.color = self.amount

            gc = out_graph.check_graph()

        # apply prices of costscheme to costs with functioin (get_costs)
        cost = get_costs(out_graph, self.costscheme)
        return [out_graph, cost]
