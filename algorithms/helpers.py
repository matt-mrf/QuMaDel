import networkx as nx
import matplotlib.pyplot as plt
from datastructure.graph import Graph
import csv


# Build a dataframe with 4 connections
def draw(graph, color_of_nodes):
    """
    Draws a graph of nodes. Nodes have the color of the color_of_nodes list of value
    """
    G = nx.from_dict_of_lists(graph)
    nx.draw(G, with_labels=True, node_color=color_of_nodes)
    plt.show()


def number_to_color(color_list):
    """
    input: list of numbers
    Transforms the number to color
    return a list of colors
    """
    colors_list = ["black", "red", "blue", "orange", "yellow", "purple", "green", "pink"]
    for i in range(len(color_list)):
        color_list[i] = colors_list[color_list[i]]
    return color_list


def make_number_list(graph):
    """
    Makes a number list from the number color of the graph
    """
    number_list = []
    for keys in graph.nodes:
        number_list.append(graph.nodes[keys].color)
    return number_list


def draw_colored_graph(graph):
    """
    Draws a graph with colored nodes.
    """
    number_list = []
    number_list = make_number_list(graph)
    color_list = number_to_color(number_list)
    draw(graph.original_graph, color_list)


def csv_to_dict(input):
    inputstring ="data/" + input + ".csv"
    data = {}
    with open(inputstring, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # row[0] is de key
            # row[1] is de lijst met adjecent nodes
            data[row[0]] = row[1].split(",")
    return data
