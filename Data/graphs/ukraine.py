import csv

input = {
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

with open('ukraine.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)

    for node in input:
        lijstje = ",".join(input[node])
        writer.writerow([node, lijstje])

data = {}
with open('ukraine.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # row[0] is de key
        # row[1] is de lijst met adjecent nodes
        data[row[0]] = row[1].split(",")

    print(data)
