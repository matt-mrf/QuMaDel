from datastructure.graph import Graph
from datastructure.node import Node
from algorithms.hill_climber import Hill_climber
from algorithms.kempe import Kempe
from algorithms.greedy import Greedy
from algorithms.randomizer import Randomizer
from algorithms.helpers import *
import copy

schemes = {
1 : {1: 12, 2: 26, 3: 27, 4: 30, 5: 37, 6: 39, 7: 41},
2 : {1: 19, 2: 20, 3: 21, 4: 23, 5: 36, 6: 37, 7: 38},
3 : {1: 16, 2: 17, 3: 31, 4: 33, 5: 36, 6: 56, 7: 57},
4 : {1: 3, 2: 34, 3: 36, 4: 39, 5: 41, 6: 43, 7: 58}
}

dict = csv_to_dict("russia")
in_graph = dict_to_graph(dict)

# make random graph, and excute different hill climber algotrithms on it
rando = Randomizer()
rand = rando.randomize_graph(in_graph, 7)

while not rand:
    rand = rando.randomize_graph(in_graph, 7)

print("Russia")
# for scheme 1:
cost_list1 = []
for i in range(5):
    rand1 = copy.deepcopy(rand)
    hc1 = Hill_climber(schemes[1])
    hc_graph1 = hc1.hill_climber_annealing(rand1)
    lowest_cost = hc_graph1[2]

    cost_list1.append(lowest_cost)
for cost in cost_list1:
    print(cost)
print("Lowest for cs1:")
print(min(cost_list1))

# for scheme 2:
cost_list2 = []
for i in range(5):
    rand2 = copy.deepcopy(rand)
    hc2 = Hill_climber(schemes[2])
    hc_graph2 = hc2.hill_climber_annealing(rand1)
    cost_list = hc_graph2[1]
    lowest_cost = cost_list[-1]

    cost_list2.append(lowest_cost)
for cost in cost_list2:
    print(cost)
print("lowest for cs2: ")
print(min(cost_list2))


# for scheme 3:
cost_list3 = []
for i in range(5):
    rand3 = copy.deepcopy(rand)
    hc3 = Hill_climber(schemes[3])
    hc_graph3 = hc3.hill_climber_annealing(rand1)
    cost_list = hc_graph3[1]
    lowest_cost = cost_list[-1]

    cost_list3.append(lowest_cost)
for cost in cost_list3:
    print(cost)
print("lowest for cs3: ")
print(min(cost_list3))

# for scheme 4:
cost_list4 = []
for i in range(5):
    rand4 = copy.deepcopy(rand)
    hc4 = Hill_climber(schemes[4])
    hc_graph4 = hc4.hill_climber_annealing(rand1)
    cost_list = hc_graph4[1]
    lowest_cost = cost_list[-1]

    cost_list4.append(lowest_cost)
for cost in cost_list4:
    print(cost)
print("lowest for cs4: ")
print(min(cost_list4))
