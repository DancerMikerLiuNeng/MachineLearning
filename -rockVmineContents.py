__author__ = "sam zhang"
import requests
import sys

target_url = "http://archive.ics.uci.edu/ml/machine-learning-databases" \
             "/undocumented/connectionist-bench/sonar/sonar.all-data"
ret = requests.get(target_url)
data = ret.text

xList = []
labels = []

for line in data.split("\n"):
    row = line.strip().split(",")
    if len(row)>1:
        xList.append(row)
nrow = len(xList)
ncol = len(xList[1])

type = [0]*3
colCounts = []


for col in range(ncol):
    for row in xList:
        try:
            a = float(row[col])
            if isinstance(a, float):
                type[0] += 1
        except ValueError:
            if len(row[col]) > 0:
                type[1] += 1
            else:
                type[2] += 1
    colCounts.append(type)
    type = [0]*3

sys.stdout.write("Col#"+"\t"+"Number"+"\t"+
                 "Strings"+ "\t"+"Other\n")
iCol = 0
for types in colCounts:
    sys.stdout.write(str(iCol)+"\t"+'\t\t'+str(types[0])+"\t\t"+
                     str(types[1])+"\t\t"+str(types[2])+"\n")
    iCol += 1
