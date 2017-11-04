import csv
file = "HRC_102117_DATA.csv"

index = []
output = []

with open( file, 'r', newline='') as f:
    reader = csv.reader(f)
    for counter, row in enumerate(reader):
        index.append(row[:1])
        output.append(row[2:3])

clean_output = []
for i in output:
    x = str(i)
    clean_output.append(x[2:-2])

week_dict = {}
for i in clean_output:
    if i not in week_dict:
        week_dict[i] = 0
    else:
        week_dict[i] += 1
print(week_dict)
