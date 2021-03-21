import csv
import pandas as pd

df = pd.read_csv('file.csv')
new_data = df[df['mass'].notna()]
# print(new_data)
new_data.to_csv('modified_file.csv')

data = []
with open('modified_file.csv', 'r') as f2:
    file2 = csv.reader(f2)
    for row in file2:
        data.append(row)
print(data[0])

for i in range(0,len(data)):
    del data[i][1]

headers = data[0]
star_data = data[1:]

with open('modified_file.csv', 'w') as f3:
    csv_writer = csv.writer(f3)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)