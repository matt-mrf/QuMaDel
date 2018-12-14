from datastructure.graph import Graph
from datastructure.node import Node
from algorithms.hill_climber import hill_climber
from algorithms.kempe import Kempe
from algorithms.helpers import *
from algorithms.randomizer import Randomizer
import csv
import random
import argparse


# costs1 = {1: 12, 2: 26, 3: 27, 4: 30, 5: 37, 6: 39, 7: 41}

parser = argparse.ArgumentParser(prog='main',
                                     usage='%(prog)s [-h] [-c] [-a] [-clr] [-cs]',
                                     description="Running this program will generate a coloured graph representing a country with given algorithm.")
parser.add_argument(
    "-c", "--country", choices=["ukraine", "china", "usa", "russia"],
    help="country to make graph of")
parser.add_argument(
    "-a", "--algorithm", choices=["random", "greedy", "kempe",
                                  "hill_climber", "hill_climber_n_opt", "hill_climber_annealing"],
    help="The algorithm that will be used to make and colour the graph.")
parser.add_argument(
    "-n", "--n_opt", choices=[1, 2, 3],
    help="Number of nodes to change when using hill_climber_n_opt", type=int)
parser.add_argument(
    "-cs", "--costscheme", choices=["1", "2", "3", "4"],
    help="Which cost scheme to calculate costs with")
args = parser.parse_args()


if args.algorithm == "random":
    dict = csv_to_dict(args.country)
    in_graph = Graph(dict)
    in_graph.create_graph()
    rando = Randomizer()
    rand = rando.randomize_graph(in_graph, 7)
    while not rand:
        rand = rando.randomize_graph(in_graph, 7)
    draw_colored_graph(rand)

# dict = csv_to_dict(args.country)
# kempe = Kempe(4)
# in_graph = Graph(dict)
# in_graph.create_graph()
# rando = Randomizer()
# rand = rando.randomize_graph(in_graph, 7)
# while not rand:
#     rand = rando.randomize_graph(in_graph, 7)
# draw_colored_graph(rand)

#

# hc = hill_climber(costs1)
#
# in_graph = Graph(input)
# in_graph.create_graph()
#
# rando = Randomizer()
# rand = rando.randomize_graph(in_graph, 7)
# while not rand:
#     rand = rando.randomize_graph(in_graph, 7)
#
# print(f"randcost: {rand.costs()}")
# draw_colored_graph(rand)
#

# out = hc.hill_climber_n_opt(rand, 2)
# # print(out.nodes)
# print(f"outcost: {out.costs()}")
# draw_colored_graph(out)
#
# out_anna = hc.hill_climber_annealing(rand)
# draw_colored_graph(out_anna)
# print(f"anna_cost: {out_anna.costs()}")

# # gc = graph_checker(in_graph)
# counter = 0
# while not in_graph.found():
#     for key, node in in_graph.nodes.items():
#         color = random.randint(1, 7)
#         node.set_color(color)
#
#     in_graph.check_graph()
#     counter += 1
#
# print(in_graph.check_graph())
# print(counter)
#
#
# for node in in_graph.nodes:
#     print('name: ' + str(in_graph.nodes[node].name) + ' color: ' + str(in_graph.nodes[node].color))
