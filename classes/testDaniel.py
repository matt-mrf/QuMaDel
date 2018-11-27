import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


graph = {
'A': ['F', 'B'],
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
'Y': ['W', 'X']
}
# Build a dataframe with 4 connections
G = nx.from_dict_of_lists(graph)
print(G)
nx.draw(G, with_labels=True)



plt.show()
