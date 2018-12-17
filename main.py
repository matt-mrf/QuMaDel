from datastructure.graph import Graph
from datastructure.node import Node
from algorithms.hill_climber import hill_climber
from algorithms.kempe import Kempe
from algorithms.randomizer import Randomizer
from algorithms.helpers import *
import csv
import random
import argparse

schemes = {
1 : {1: 12, 2: 26, 3: 27, 4: 30, 5: 37, 6: 39, 7: 41},
2 : {1: 19, 2: 20, 3: 21, 4: 23, 5: 36, 6: 37, 7: 38},
3 : {1: 16, 2: 17, 3: 31, 4: 33, 5: 36, 6: 56, 7: 57},
4 : {1: 3, 2: 34, 3: 36, 4: 39, 5: 41, 6: 43, 7: 58}
}

parser = argparse.ArgumentParser(prog='main',
                                 usage='%(prog)s [-h] [-c] [-a] [-clr] [-n] [-cs]',
                                 description="Running this program will generate a coloured graph representing a country with given algorithm.")
parser.add_argument(
    "-c", "--country", choices=["ukraine", "china", "usa", "russia"],
    help="Country to make graph of")
parser.add_argument(
    "-a", "--algorithm", choices=["random", "greedy", "kempe",
                                  "hill_climber", "hill_climber_n_opt",
                                  "hill_climber_annealing"],
    help="The algorithm that will be used to make and colour the graph.")
parser.add_argument(
    "-clr", "--colors", choices=[1, 2, 3, 4, 5, 6, 7],
    help="Which cost scheme to calculate costs with", type=int)
parser.add_argument(
    "-n", "--n_opt", choices=[1, 2, 3],
    help="Number of nodes to change when using hill_climber_n_opt", type=int)
parser.add_argument(
    "-cs", "--costscheme", choices=[1, 2, 3, 4],
    help="Which cost scheme to calculate costs with", type=int)
args = parser.parse_args()

# process the input
dict = csv_to_dict(args.country)
in_graph = dict_to_graph(dict)
colors = args.colors
n = args.n_opt
scheme = schemes[args.costscheme]

# from empty dict fill in random graph
if args.algorithm == "random":
    if not args.colors:
        print("Error: ")
        print("please provide an amount of colors to use with -clr [1,2,3,4,5,6,7]")
    else:
        rando = Randomizer()
        rand = rando.randomize_graph(in_graph, colors)

        while not rand:
            rand = rando.randomize_graph(in_graph, colors)

        draw_colored_graph(rand)
elif args.algorithm == "kempe":
    kempe = Kempe(colors)

    kempe_graph = kempe.execute_kempe(in_graph)

    draw_colored_graph(kempe_graph)
elif args.algorithm == "hill_climber":
    if not scheme:
        print("Error:")
        print("Please provide a costscheme with -cs [1,2,3,4]")
    else:
        hc = hill_climber(scheme)

        rando = Randomizer()
        random_graph = rando.randomize_graph(in_graph, 7)

        while not random_graph:
            random_graph = rando.randomize_graph(in_graph, 7)

        hc_graph = hc.hill_climber(random_graph)
        cost_list = hc_graph[1]

        draw_cost_list(cost_list, args.country, "hill-climber")
        draw_colored_graph(hc_graph[0])
elif args.algorithm == "hill_climber_n_opt":
    if not scheme:
        print("Error:")
        print("Please provide a costscheme with -cs [1,2,3,4]")
    elif not n:
        print("Error:")
        print("Please provide an n for n-opt with -n [1,2,3]")
    else:
        hc = hill_climber(scheme)

        rando = Randomizer()
        random_graph = rando.randomize_graph(in_graph, 7)

        while not random_graph:
            random_graph = rando.randomize_graph(in_graph, 7)

        hc_graph = hc.hill_climber_n_opt(random_graph, n)
        cost_list = hc_graph[1]

        draw_cost_list(cost_list, args.country, "hill climber " + str(n) + "-opt")
        draw_colored_graph(hc_graph[0])
elif args.algorithm == "hill_climber_annealing":
    if not scheme:
        print("Error:")
        print("Please provide a costscheme with -cs [1,2,3,4]")
    else:
        hc = hill_climber(scheme)

        rando = Randomizer()
        random_graph = rando.randomize_graph(in_graph, 7)

        while not random_graph:
            random_graph = rando.randomize_graph(in_graph, 7)

        hc_graph = hc.hill_climber_annealing(random_graph)
        cost_list = hc_graph[1]

        draw_cost_list(cost_list, args.country, "hill-climber simulated annealing")
        draw_colored_graph(hc_graph[0])

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
