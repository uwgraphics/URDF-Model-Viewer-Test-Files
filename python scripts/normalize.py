import csv
import sys
import math

maxRows = 1
outputs = []

argIndex = 0
for input in sys.argv:
    if(argIndex == 1):
        maxRows = int(input)
    elif(argIndex >= 2):
        index = 0
        offset = 0
        data = []
        with open(input, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                if(index == 0):
                    data.append(row)
                else:
                    row[0] = float(row[0]) / 1000000000
                    if(index == 1):
                        offset = row[0]                        
                    data.append(row)
                index += 1
        out = input.replace(".csv", "_out.csv")
        output = [data, out, offset, index]
        outputs.append(output)
    argIndex += 1

offset = -1
for output in outputs:
    if(output[2] < offset or offset < 0):
        offset = output[2]
        
print("offset", offset)

for output in outputs:
    skip = math.ceil((output[3] / maxRows))
    with open(output[1], 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter = ',', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')
        index = 0
        for row in output[0]:
            if(index == 0):
                writer.writerow(row)
            else:
                row[0] -= offset
                if(index % skip == 1 or skip == 1):
                    writer.writerow(row)
            index += 1