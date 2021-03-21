import csv
import pandas as pd

df = pd.read_csv('file2.csv')
new_data = df[df['name'].notna()]
new_data = df[df['distance'].notna()]
new_data = df[df['mass'].notna()]
new_data = df[df['radius'].notna()]
# print(new_data)
new_data.to_csv('modified_file2.csv')

data = []
with open('modified_file2.csv', 'r') as f2:
    file2 = csv.reader(f2)
    for row in file2:
        data.append(row)
print(data[0])

for i in range(0,len(data)):
    del data[i][1]

headers = data[0]
star_data = data[1:]

for data in star_data:
    data[4] = float(data[4]) * 0.102763

for data in star_data:
    data[3] = float(data[3]) * 0.000954588

with open('modified_file2.csv', 'w') as f3:
    csv_writer = csv.writer(f3)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)