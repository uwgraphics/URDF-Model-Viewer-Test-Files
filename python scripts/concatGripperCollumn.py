import csv
import sys

rowIndex = 0
armData = []

if(len(sys.argv) != 4):
    sys.exit("Need for params: armData, robotData, output")
    
armFile = sys.argv[1]
robotMotionFile = sys.argv[2]
out = sys.argv[3]
        
with open(armFile, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        if(rowIndex == 0):
            armData.append([(row[0]), (row[1])])
        else:
            armData.append([float(row[0]), float(row[1])])
        rowIndex += 1

armData.pop(0)

rowIndex = 0
robotData = []
with open(robotMotionFile, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        if(rowIndex > 0):
            t1 = 0
            t2 = 0
            for i in range(len(armData)):
                if(float(row[0]) >= armData[i][0]):
                    t1 = i
                    t2 = i + 1 if i + 1 < len(armData) else i
            if(t1 == t2):
                row.append(armData[t1][1])
            else:
                u = (float(row[0]) - armData[t1][0]) / (armData[t2][0] - armData[t1][0])
                v = armData[t1][1] + u * (armData[t2][1] - armData[t1][1])
                row.append(v)
        robotData.append(row)
        rowIndex += 1
        
with open(out, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')
    index = 0
    for row in robotData:
        writer.writerow(row)