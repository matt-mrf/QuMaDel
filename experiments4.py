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

dict = csv_to_dict("ukraine")
in_graph = dict_to_graph(dict)

# make random graph, and excute different hill climber algotrithms on it
rando = Randomizer()
rand = rando.randomize_graph(in_graph, 7)

while not rand:
    rand = rando.randomize_graph(in_graph, 7)

print("Ukraine")
# for scheme 1:
cost_list1 = []
cost_list1_x = []
for i in range(10):
    rand1 = copy.deepcopy(rand)
    rand1x = copy.deepcopy(rand)

    hc1 = Hill_climber(schemes[1])

    hc_graph1 = hc1.hill_climber_n_opt(rand1, 2)
    hc_graph1x = hc1.hill_climber(rand1x)

    lowest_cost = hc_graph1[2]
    lowest_cost_x = hc_graph1x[2]

    cost_list1.append(lowest_cost)
    cost_list1_x.append(lowest_cost_x)

for cost in cost_list1:
    print(cost)

print("Lowest for cs1 2-opt:")
print(min(cost_list1))

print("---------------------")
for cost in cost_list1_x:
    print(cost)

print("Lowest for cs1 hill climber:")
print(min(cost_list1_x))

print("-------------------------------------------------")

# for scheme 2:
cost_list2 = []
cost_list2_x = []
for i in range(10):
    rand2 = copy.deepcopy(rand)
    rand2x = copy.deepcopy(rand)

    hc2 = Hill_climber(schemes[2])

    hc_graph2 = hc1.hill_climber_n_opt(rand2, 2)
    hc_graph2x = hc1.hill_climber(rand2x)

    lowest_cost = hc_graph2[2]
    lowest_cost_x = hc_graph2x[2]

    cost_list2.append(lowest_cost)
    cost_list2_x.append(lowest_cost_x)

for cost in cost_list2:
    print(cost)

print("Lowest for cs2 2-opt:")
print(min(cost_list2))

print("---------------------")
for cost in cost_list2_x:
    print(cost)

print("Lowest for cs2 hill climber:")
print(min(cost_list2_x))

print("-------------------------------------------------")

# for scheme 3:
cost_list3 = []
cost_list3_x = []
for i in range(10):
    rand3 = copy.deepcopy(rand)
    rand3x = copy.deepcopy(rand)

    hc3 = Hill_climber(schemes[3])

    hc_graph3 = hc1.hill_climber_n_opt(rand3, 2)
    hc_graph3x = hc1.hill_climber(rand3x)

    lowest_cost = hc_graph3[2]
    lowest_cost_x = hc_graph3x[2]

    cost_list3.append(lowest_cost)
    cost_list3_x.append(lowest_cost_x)

for cost in cost_list3:
    print(cost)

print("Lowest for cs3 2-opt:")
print(min(cost_list3))

print("---------------------")
for cost in cost_list3_x:
    print(cost)

print("Lowest for cs3 hill climber:")
print(min(cost_list3_x))

print("-------------------------------------------------")

# for scheme 4:
cost_list4 = []
cost_list4_x = []
for i in range(5):
    rand4 = copy.deepcopy(rand)
    rand4x = copy.deepcopy(rand)

    hc4 = Hill_climber(schemes[4])

    hc_graph4 = hc1.hill_climber_n_opt(rand4, 2)
    hc_graph4x = hc1.hill_climber(rand4x)

    lowest_cost = hc_graph4[2]
    lowest_cost_x = hc_graph4x[2]

    cost_list4.append(lowest_cost)
    cost_list4_x.append(lowest_cost_x)

for cost in cost_list4:
    print(cost)

print("Lowest for cs4 2-opt:")
print(min(cost_list4))

print("---------------------")
for cost in cost_list4_x:
    print(cost)

print("Lowest for cs4 hill climber:")
print(min(cost_list4_x))

print("-------------------------------------------------")
