import csv

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

with open('ukraine.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)

    for node in input:
        lijstje = ",".join(input[node])
        writer.writerow([node, lijstje])

data = {}
with open('ukraine.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # row[0] is the key
        # row[1] is the list with adjecent nodes
        data[row[0]] = row[1].split(",")

return data