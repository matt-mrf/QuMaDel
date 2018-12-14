import csv

input = {'AL': ['FL', 'GA', 'MS', 'TN'],
         'FL': ['AL', 'GA'],
         'GA': ['AL', 'FL', 'NC', 'SC', 'TN'],
         'MS': ['AL', 'AR', 'LA', 'TN'],
         'TN': ['AL', 'AR', 'GA', 'KY', 'MO', 'MS', 'NC', 'VA'],
         'AR': ['LA', 'MO', 'MS', 'OK', 'TN', 'TX'],
         'LA': ['AR', 'MS', 'TX'],
         'MO': ['AR', 'IA', 'IL', 'KS', 'KY', 'NE', 'OK', 'TN'],
         'OK': ['AR', 'CO', 'KS', 'MO', 'NM', 'TX'],
         'TX': ['AR', 'LA', 'NM', 'OK'],
         'AZ': ['CA', 'CO', 'NM', 'NV', 'UT'],
         'CA': ['AZ', 'NV', 'OR'],
         'CO': ['AZ', 'KS', 'NE', 'NM', 'OK', 'UT', 'WY'],
         'NM': ['AZ', 'CO', 'OK', 'TX', 'UT'],
         'NV': ['AZ', 'CA', 'ID', 'OR', 'UT'],
         'UT': ['AZ', 'CO', 'ID', 'NM', 'NV', 'WY'],
         'OR': ['CA', 'ID', 'NV', 'WA'],
         'KS': ['CO', 'MO', 'NE', 'OK'],
         'NE': ['CO', 'IA', 'KS', 'MO', 'SD', 'WY'],
         'WY': ['CO', 'ID', 'MT', 'NE', 'SD', 'UT'],
         'CT': ['MA', 'NY', 'RI'],
         'MA': ['CT', 'NH', 'NY', 'RI', 'VT'],
         'NY': ['CT', 'MA', 'NJ', 'PA', 'VT'],
         'RI': ['CT', 'MA'],
         'DC': ['MD', 'VA'],
         'MD': ['DC', 'DE', 'PA', 'VA', 'WV'],
         'VA': ['DC', 'KY', 'MD', 'NC', 'TN', 'WV'],
         'DE': ['MD', 'NJ', 'PA'],
         'NJ': ['DE', 'NY', 'PA'],
         'PA': ['DE', 'MD', 'NJ', 'NY', 'OH', 'WV'],
         'NC': ['GA', 'SC', 'TN', 'VA'],
         'SC': ['GA', 'NC'],
         'IA': ['MN', 'MO', 'NE', 'SD', 'WI', 'IL'],
         'MN': ['IA', 'ND', 'SD', 'WI'],
         'SD': ['IA', 'MN', 'MT', 'ND', 'NE', 'WY'],
         'WI': ['IA', 'IL', 'MI', 'MN'],
         'ID': ['MT', 'NV', 'OR', 'UT', 'WA', 'WY'],
         'MT': ['ID', 'ND', 'SD', 'WY'],
         'WA': ['ID', 'OR'],
         'IL': ['IA', 'IN', 'KY', 'MO', 'WI'],
         'IN': ['IL', 'KY', 'MI', 'OH'],
         'KY': ['IL', 'IN', 'MO', 'OH', 'TN', 'VA', 'WV'],
         'MI': ['IN', 'OH', 'WI'],
         'OH': ['IN', 'KY', 'MI', 'PA', 'WV'],
         'WV': ['KY', 'MD', 'OH', 'PA', 'VA'],
         'NH': ['MA', 'ME', 'VT'],
         'VT': ['MA', 'NH', 'NY'],
         'ME': ['NH'],
         'ND': ['MN', 'MT', 'SD']
         }

with open('usa.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)

    for node in input:
        lijstje = ",".join(input[node])
        writer.writerow([node, lijstje])

data = {}
with open('usa.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # row[0] is de key
        # row[1] is de lijst met adjecent nodes
        data[row[0]] = row[1].split(",")

    print(data)
