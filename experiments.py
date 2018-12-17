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

# make random graph, and excute different hill climber algotrithms on it
rando = Randomizer()
rand = rando.randomize_graph(in_graph, colors)

while not rand:
    rand = rando.randomize_graph(in_graph, colors)

hc = hill_climber
