from graph import Graph
from node import Node
from graph_checker import graph_checker
import random

input = {'A': ['F', 'B'],
'B': ['A', 'F', 'E', 'D', 'C'],
'C': ['B', 'D'],
'D': ['C', 'B', 'E', 'H'],
'E': ['D', 'B', 'F', 'G', 'H'],
'F': ['A', 'B', 'E', 'G', 'J'],
'G': ['E', 'F', 'J', 'I', 'H'],
'H': ['D', 'E', 'G', 'I'],
'I': ['H', 'G', 'J', 'K', 'N', 'O', 'L'],
'J': ['F', 'G', 'I', 'K'],
'K': ['J', 'I', 'N', 'R', 'M'],
'L': ['I', 'O', 'P'],
'M': ['Q', 'K'],
'N': ['K', 'R', 'O', 'I'],
'O': ['I', 'N', 'R', 'U', 'P', 'L'],
'P': ['L', 'O', 'U', 'S'],
'Q': ['M', 'R'],
'R': ['K', 'Q', 'W', 'U', 'O', 'N'],
'S': ['P', 'U', 'V', 'T'],
'T': ['S'],
'U': ['R', 'W', 'X', 'V', 'S', 'P', 'O'],
'V': ['S', 'U', 'X'],
'W': ['R', 'U', 'X', 'Y'],
'X': ['V', 'U', 'W', 'Y'],
'Y': ['W', 'X']}

ukraine = Graph(input)
ukraine.create_graph()

for key, node in ukraine.nodes.items():
    color = random.randint(1, 5)
    node.set_color(color)

print(ukraine.nodes)

gc = graph_checker(ukraine)
counter = 0
while not gc.found():
    gc.check_graph()

    for key, node in ukraine.nodes.items():
        color = random.randint(1, 5)
        node.set_color(color)

    counter += 1
print(counter)
