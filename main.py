from datastructure.graph import Graph
from datastructure.node import Node
from algorithms.hill_climber import Hill_climber
from algorithms.kempe import Kempe
from algorithms.greedy import Greedy
from algorithms.randomizer import Randomizer
from algorithms.helpers import *
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
    help="The amount of colors to use", type=int)
parser.add_argument(
    "-n", "--n_opt", choices=[1, 2, 3, 4, 5],
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

if args.costscheme:
    scheme = schemes[args.costscheme]


# from empty dict fill in random graph
if args.algorithm == "random":
    if not args.costscheme:
        print("Error:")
        print("Please provide a costscheme with -cs [1,2,3,4]")
    elif not colors:
        print("Error: ")
        print("please provide an amount of colors to use with -clr [1,2,3,4,5,6,7]")
    else:
        rando = Randomizer()
        rand = rando.randomize_graph(in_graph, colors)

        while not rand:
            rand = rando.randomize_graph(in_graph, colors)

        cost = get_costs(rand, scheme)

        print(f"Costs for this graph, with costsscheme {args.costscheme} are: {cost}")
        draw_colored_graph(rand)
elif args.algorithm == "kempe":
    if not args.costscheme:
        print("Error:")
        print("Please provide a costscheme with -cs [1,2,3,4]")
    elif not colors:
        print("Error: ")
        print("please provide an amount of colors to use with -clr [1,2,3,4,5,6,7]")
    else:
        kempe = Kempe(colors, scheme)

        kempe_graph = kempe.execute_kempe(in_graph)

        graph = kempe_graph[0]
        cost = kempe_graph[1]
        print(f"Costs for this graph, with costsscheme {args.costscheme} are: {cost}")
        draw_colored_graph(graph)
elif args.algorithm == "greedy":
    if not args.costscheme:
        print("Error:")
        print("Please provide a costscheme with -cs [1,2,3,4]")
    elif not colors:
        print("Error: ")
        print("please provide an amount of colors to use with -clr [1,2,3,4,5,6,7]")
    else:
        greedy = Greedy(in_graph, scheme)

        greedy_graph = greedy.greedy_fill()

        graph = greedy_graph[0]
        cost = greedy_graph[1]

        print(f"Costs for this graph, with costsscheme {args.costscheme} are: {cost}")
        draw_colored_graph(graph)
elif args.algorithm == "hill_climber":
    if not args.costscheme:
        print("Error:")
        print("Please provide a costscheme with -cs [1,2,3,4]")
    else:
        hc = Hill_climber(scheme)

        rando = Randomizer()
        random_graph = rando.randomize_graph(in_graph, 7)

        while not random_graph:
            random_graph = rando.randomize_graph(in_graph, 7)

        hc_graph = hc.hill_climber(random_graph)
        cost_list = hc_graph[1]
        lowest_cost = cost_list[-1]

        print(f"The lowest cost is {lowest_cost}")
        draw_cost_list(cost_list, args.country, "hill-climber")
        draw_colored_graph(hc_graph[0])
elif args.algorithm == "hill_climber_n_opt":
    if not args.costscheme:
        print("Error:")
        print("Please provide a costscheme with -cs [1,2,3,4]")
    elif not n:
        print("Error:")
        print("Please provide an n for n-opt with -n [1,2,3]")
    else:
        hc = Hill_climber(scheme)

        rando = Randomizer()
        random_graph = rando.randomize_graph(in_graph, 7)

        while not random_graph:
            random_graph = rando.randomize_graph(in_graph, 7)

        hc_graph = hc.hill_climber_n_opt(random_graph, n)
        cost_list = hc_graph[1]
        lowest_cost = cost_list[-1]

        print(f"The lowest cost is {lowest_cost}")
        draw_cost_list(cost_list, args.country, "hill climber " + str(n) + "-opt")
        draw_colored_graph(hc_graph[0])
elif args.algorithm == "hill_climber_annealing":
    if not args.costscheme:
        print("Error:")
        print("Please provide a costscheme with -cs [1,2,3,4]")
    else:
        hc = Hill_climber(scheme)

        rando = Randomizer()
        random_graph = rando.randomize_graph(in_graph, 7)

        while not random_graph:
            random_graph = rando.randomize_graph(in_graph, 7)

        hc_graph = hc.hill_climber_annealing(random_graph)
        cost_list = hc_graph[1]
        lowest_cost = cost_list[-1]

        print(f"The lowest cost is {lowest_cost}")
        draw_cost_list(cost_list, args.country, "hill-climber simulated annealing")
        draw_colored_graph(hc_graph[0])
