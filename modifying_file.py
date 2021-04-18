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
# print(data[0])

for i in range(0,len(data)):
    del data[i][1]

headers = data[0]
star_data = data[1:]

for data in star_data:
    if data[2] != '?':
        data[2] = data[2].replace(',', '')
        data[2] = data[2].replace('[', ' ')
        data[2] = float(data[2].split(' ')[0])
        # print(data[2])
    
    if data[3] != '?':
        data[3] = data[3].replace('-', ' ')
        data[3] = data[3].replace('â€“', ' ')
        data[3] = data[3].replace('<', '')
        data[3] = float(data[3].split(' ')[0])
        # print(data[3])
    else:
        data[3] = data[3].replace('?', '')

    if data[4] != '?':
        data[4] = data[4].replace('-', ' ')
        data[4] = data[4].replace('â€“', ' ')
        data[4] = data[4].replace('Â´', ' ')
        data[4] = data[4].replace(',', '')
        data[4] = float(data[4].split(' ')[0])
        # print(data[4])
    else:
        data[4] = data[4].replace('?', '')

with open('modified_file.csv', 'w') as f3:
    csv_writer = csv.writer(f3)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)