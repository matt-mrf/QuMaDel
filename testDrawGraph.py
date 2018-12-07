import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


input2 = {
    '1': ['2', '4', '6'],
    '2': ['1', '4', '5', '3'],
    '3': ['2', '5', '7', '8'],
    '4': ['1', '6', '5', '2'],
    '5': ['4', '6', '10', '11', '9', '7', '3', '2'],
    '6': ['1', '4', '5', '10', '12'],
    '7': ['5', '9', '16', '8', '3'],
    '8': ['3', '7', '16', '17'],
    '9': ['5', '11', '15', '16', '7'],
    '10': ['6', '12', '11', '5'],
    '11': ['10', '12', '13', '14', '15', '9', '5'],
    '12': ['6', '10', '11', '13', '25', '28', '29', '30'],
    '13': ['12', '25', '14', '11'],
    '14': ['13', '25', '24', '19', '15', '11'],
    '15': ['11', '14', '19', '18', '16', '9'],
    '16': ['9', '8', '7', '15', '18', '17'],
    '17': ['8', '16', '18', '20'],
    '18': ['15', '19', '21', '20', '17', '16'],
    '19': ['14', '23', '18', '15', '21'],
    '20': ['17', '18', '21'],
    '21': ['20', '18', '19', '23', '22'],
    '22': ['21', '23'],
    '23': ['19', '21', '22', '24'],
    '24': ['25', '14', '23'],
    '25': ['24', '14', '13', '12', '26', '27', '28'],
    '26': ['25', '27'],
    '27': ['25', '26'],
    '28': ['25', '12', '29'],
    '29': ['28', '30', '12'],
    '30': ['29', '12']
}



# Build a dataframe with 4 connections
def draw(graph, color_of_nodes):
    """
    Draws a graph of nodes. Nodes have the color of the color_of_nodes list of value
    """
    G = nx.from_dict_of_lists(graph)
    nx.draw(G, with_labels=True, node_color=color_of_nodes)
    plt.show()

def numberList_to_colorList(color_list):
    """
    Transforms the number color to actual color
    return a list
    """
    colors_list = ["black", "red", "blue", "orange", "yellow", "purple", "green", "pink"]
    for i in range(len(color_list)):
        color_list[i] = colors_list[color_list[i]]
    return color_list


def numberList(graph):
    """
    Makes a number list from the numbercolor of the graph
    """
    number_list = []
    for keys in graph.nodes:
        number_list.append(graph.nodes[keys].color)
    return number_list


def draw_colored_graph(graph):
    """
    Draws a graph with colored nodes.
    """
    number_list = numberList(graph)
    color_list = numberList_to_colorList(number_list)
    draw(graph.original_graph, color_list)


if __name__ == "__main__":
    graphUkr = Graph(input)
    graphUkr.create_graph()
    kempe = Kempe(5)
    graphUkr = kempe.execute_kempe(graphUkr)
    print(graphUkr.nodes)
    draw_colored_graph(graphUkr)
