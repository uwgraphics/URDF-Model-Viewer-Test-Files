import csv
import sys

fileName = sys.argv[1]
print("in: " + fileName)

output = ""
if(len(sys.argv) >= 3):
    output = sys.argv[2]
    print("out: " + output)
else:
    output = fileName + "_modified.csv"

index = 0
data = []

with open(fileName, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        if(index != 0):
            row = map(lambda element: float(element), row)
            # row[0] /= 1000000000
        data.append(row)
        index += 1

with open(output, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')
    for row in data:
        writer.writerow(row)