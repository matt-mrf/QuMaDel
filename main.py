from datastructure.graph import Graph
from datastructure.node import Node
from algorithms.hill_climber import hill_climber
from algorithms.kempe import Kempe
from algorithms.helpers import *
import random

input = {
    '1': ['6', '2'],
    '2': ['1', '6', '5', '4', '3'],
    '3': ['2', '4'],
    '4': ['3', '2', '5', '8'],
    '5': ['4', '2', '6', '7', '8'],
    '6': ['1', '2', '5', '7', '10'],
    '7': ['5', '6', '10', '9', '8'],
    '8': ['4', '5', '7', '9'],
    '9': ['8', '7', '10', '11', '14', '15', '12'],
    '10': ['6', '7', '9', '11'],
    '11': ['10', '9', '14', '18', '13'],
    '12': ['9', '15', '16'],
    '13': ['17', '11'],
    '14': ['11', '18', '15', '9'],
    '15': ['9', '14', '18', '21', '16', '12'],
    '16': ['12', '15', '21', '19'],
    '17': ['13', '18'],
    '18': ['11', '17', '23', '21', '15', '14'],
    '19': ['16', '21', '22', '20'],
    '20': ['19'],
    '21': ['18', '23', '24', '22', '19', '16', '15'],
    '22': ['19', '21', '24'],
    '23': ['18', '21', '24', '25'],
    '24': ['22', '21', '23', '25'],
    '25': ['23', '24']
}


in_graph = Graph(input)
in_graph.create_graph()

kempe = Kempe(4)

in_graph = Graph(input)
in_graph.create_graph()

out = kempe.execute_kempe(in_graph)

draw_colored_graph(out)

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
