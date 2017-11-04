import csv
import sys
import json

# EDIT THIS LIST WITH YOUR REQUIRED JSON KEY NAMES
fieldnames = ["firstname", "secondname", "age"]
filename = "small-excel.xlsx"

print ("Opening CSV file: ", filename)
f = open(filename, 'r')

csv_reader = csv.DictReader(f, fieldnames)
json_filename = filename.split(".")[0] + ".json"
print ("Saving JSON to file: ", json_filename)
jsonf = open(json_filename, 'w')
data = json.dumps([r for r in csv_reader])
jsonf.write(data)
f.close()
jsonf.close()
