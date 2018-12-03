from classes.graph import Graph
from classes.hill_climber import hill_climber
from classes.greedy import greedy
from classes.kempe import Kempe
from classes.randomizer import Randomizer
import random


costs1 = {1: 12, 2: 26, 3: 27, 4: 30, 5: 37, 6: 39, 7: 41}

# input = {
#     "A": ["B", "E"],
#     "B": ["A", "C", "E"],
#     "C": ["B", "D"],
#     "D": ["C", "E"],
#     "E": ["A", "B", "D", "F"],
#     "F": ["E"],
# }


# input = {
#     '1': ['6', '2'],
#     '2': ['1', '6', '5', '4', '3'],
#     '3': ['2', '4'],
#     '4': ['3', '2', '5', '8'],
#     '5': ['4', '2', '6', '7', '8'],
#     '6': ['1', '2', '5', '7', '10'],
#     '7': ['5', '6', '10', '9', '8'],
#     '8': ['4', '5', '7', '9'],
#     '9': ['8', '7', '10', '11', '14', '15', '12'],
#     '10': ['6', '7', '9', '11'],
#     '11': ['10', '9', '14', '18', '13'],
#     '12': ['9', '15', '16'],
#     '13': ['17', '11'],
#     '14': ['11', '18', '15', '9'],
#     '15': ['9', '14', '18', '21', '16', '12'],
#     '16': ['12', '15', '21', '19'],
#     '17': ['13', '18'],
#     '18': ['11', '17', '23', '21', '15', '14'],
#     '19': ['16', '21', '22', '20'],
#     '20': ['19'],
#     '21': ['18', '23', '24', '22', '19', '16', '15'],
#     '22': ['19', '21', '24'],
#     '23': ['18', '21', '24', '25'],
#     '24': ['22', '21', '23', '25'],
#     '25': ['23', '24']
# }

# input = {
#     '1': ['2', '4', '6'],
#     '2': ['1', '4', '5', '3'],
#     '3': ['2', '5', '7', '8'],
#     '4': ['1', '6', '5', '2'],
#     '5': ['4', '6', '10', '11', '9', '7', '3', '2'],
#     '6': ['1', '4', '5', '10', '12'],
#     '7': ['5', '9', '16', '8', '3'],
#     '8': ['3', '7', '16', '17'],
#     '9': ['5', '11', '15', '16', '7'],
#     '10': ['6', '12', '11', '5'],
#     '11': ['10', '12', '13', '14', '15', '9', '5'],
#     '12': ['6', '10', '11', '13', '25', '28', '29', '30'],
#     '13': ['12', '25', '14', '11'],
#     '14': ['13', '25', '24', '19', '15', '11'],
#     '15': ['11', '14', '19', '18', '16', '9'],
#     '16': ['9', '8', '7', '15', '18', '17'],
#     '17': ['8', '16', '18', '20'],
#     '18': ['15', '19', '21', '20', '17', '16'],
#     '19': ['14', '23', '18', '15', '21'],
#     '20': ['17', '18', '21'],
#     '21': ['20', '18', '19', '23', '22'],
#     '22': ['21', '23'],
#     '23': ['19', '21', '22', '24'],
#     '24': ['25', '14', '23'],
#     '25': ['24', '14', '13', '12', '26', '27', '28'],
#     '26': ['25', '27'],
#     '27': ['25', '26'],
#     '28': ['25', '12', '29'],
#     '29': ['28', '30', '12'],
#     '30': ['29', '12']
# }
#
input = {
    '1': ['23'],
    '2': ['16', '18', '56', '66', '74', '90'],
    '3': ['75', '38', '17'],
    '4': ['17', '19', '22', '42'],
    '5': ['20', '26', '8'],
    '6': ['15', '20', '26', '7'],
    '7': ['9', '26', '6'],
    '8': ['5', '26', '61', '34', '30'],
    '9': ['23', '26', '7'],
    '10': ['51', '29', '47', '35'],
    '11': ['29', '83', '89', '86', '66', '90', '43'],
    '12': ['52', '21', '43', '16'],
    '13': ['62', '52', '58', '73', '21'],
    '14': ['24', '38', '75', '28', '27', '49', '87'],
    '15': ['20', '6'],
    '16': ['21', '12', '43', '18', '2', '56', '63', '73'],
    '17': ['4', '19', '3', '38', '24'],
    '18': ['90', '2', '16', '43'],
    '19': ['24', '17', '42', '4'],
    '20': ['5', '26', '6', '15'],
    '21': ['12', '16', '73', '13', '52'],
    '22': ['54', '42', '4'],
    '23': ['1', '9', '26', '61'],
    '24': ['89', '86', '70', '42', '19', '17', '38', '14'],
    '25': ['27'],
    '26': ['20', '5', '8', '7', '9', '23', '61', '6'],
    '27': ['28', '14', '49', '79', '25', '65'],
    '28': ['75', '14', '79', '27'],
    '29': ['10', '83', '11', '43', '35'],
    '30': ['8', '34'],
    '31': ['46', '36'],
    '32': ['67', '40', '57', '46'],
    '33': ['62', '52', '44', '76', '50'],
    '34': ['61', '8', '30', '64', '36'],
    '35': ['53', '47', '10', '29', '43', '37', '69', '76'],
    '36': ['46', '31', '48', '68', '34', '61', '64'],
    '37': ['44', '52', '43', '35', '76'],
    '38': ['17', '24', '14', '3', '75'],
    '39': [],
    '40': ['32', '57', '71', '50', '67'],
    '41': ['49', '87'],
    '42': ['54', '70', '24', '19', '4', '22'],
    '43': ['12', '52', '37', '35', '29', '11', '18', '16', '90'],
    '44': ['33', '76', '52', '37'],
    '45': ['72', '66', '74'],
    '46': ['32', '57', '48', '36', '31'],
    '47': ['78', '53', '35', '10', '60'],
    '48': ['57', '46', '36', '68', '62', '71'],
    '49': ['27', '41', '14', '87'],
    '50': ['77', '33', '62', '71', '40', '67', '69', '76'],
    '51': ['10'],
    '52': ['13', '21', '12', '43', '37', '44', '33', '62'],
    '53': ['60', '69', '47', '35'],
    '54': ['55', '70', '42', '22'],
    '55': ['72', '86', '70', '54'],
    '56': ['64', '63', '16', '2', '74'],
    '57': ['32', '40', '71', '48', '46'],
    '58': ['68', '13', '73', '64', '62'],
    '60': ['67', '69', '53', '47'],
    '61': ['23', '26', '8', '34', '36'],
    '62': ['48', '68', '58', '13', '52', '33', '50', '71'],
    '63': ['64', '73', '16', '56'],
    '64': ['36', '34', '68', '58', '73', '63', '56'],
    '65': ['27'],
    '66': ['90', '2', '74', '45', '72', '11', '86'],
    '67': ['32', '40', '50', '69', '60'],
    '68': ['36', '64', '58', '48', '62'],
    '69': ['50', '35', '60', '67', '76', '53'],
    '70': ['54', '55', '86', '24', '42'],
    '71': ['40', '50', '48', '62', '57'],
    '72': ['45', '55', '86', '66'],
    '73': ['58', '13', '21', '16', '63', '64'],
    '74': ['56', '2', '66', '45'],
    '75': ['3', '38', '14', '28'],
    '76': ['69', '50', '33', '44', '37', '35'],
    '77': ['50'],
    '78': ['47'],
    '79': ['28', '27'],
    '83': ['11', '89', '29'],
    '86': ['66', '72', '70', '24', '89', '11', '55'],
    '87': ['14', '49', '41'],
    '89': ['11', '86', '83', '24'],
    '90': ['43', '11', '66', '18', '2']
}

kempe = Kempe(4)

in_graph = Graph(input)
in_graph.create_graph()

rando = Randomizer()
rand = rando.randomize_graph(in_graph, 7)
while not rand:
    rand = rando.randomize_graph(in_graph, 7)



# for key, node in in_graph.nodes.items():
#     color = random.randint(1, 4)
#     node.set_color(color)

# greedy = greedy(in_graph)
#
hc = hill_climber(costs1)
hc.hill_climber(rand)

cost_list = []
for i in range(100):
    in_graph = Graph(input)
    in_graph.create_graph()
    greedy = greedy(in_graph)
    hc_graph = greedy.hillclimber_fill()
    hc = hill_climber(costs1)
    cost_list.append(hc.hill_climber(hc_graph))
    print(cost_list)
    print(min(cost_list))
# hc = hill_climber(in_graph)
# hc.hillclimber_fill()
