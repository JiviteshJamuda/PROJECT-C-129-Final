import csv

data1 = []
data2 = []

with open('modified_file.csv', 'r') as f:
    file = csv.reader(f)
    for i in file:
        data1.append(i)

with open('modified_file2.csv', 'r') as f1:
    file = csv.reader(f1)
    for j in file:
        data2.append(j)

planet_data1 = data1[1:]
planet_data2 = data2[1:]

headers = data1[0]
headers[0] = 'Serial number'
planet_data = []

for index, data_row in enumerate(planet_data1):
    planet_data.append(planet_data1[index])

for index, data_row in enumerate(planet_data2):
    planet_data.append(planet_data2[index])

with open('merged_data.csv', 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)