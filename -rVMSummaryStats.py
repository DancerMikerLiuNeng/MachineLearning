__author__ = "sam zhang"
import requests
import sys
import numpy as np
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

col = 3
colData = []
#generate summary staticstics for column 3
for row in xList:
    try:
        #print(row[col])
        colData.append(float(row[col]))
        # print(float(row[col]))
    except:
        pass
print(colData)
colArray = np.array(colData)
colMean = np.mean(colArray)
colsd = np.std(colArray)
sys.stdout.write("Mean = " + "\t" + str(colMean) + "\t\t" +
                 "Standard Deviation = " + "\t" + str(colsd) + "\n")
#calculate quantile boundaries
ntiles = 4
percentBdry = []
for i in range(ntiles+1):
    percentBdry.append(np.percentile(colArray, i*(100)/ntiles))
sys.stdout.write("\nBoundaries for 4 Equal Percentiles \n")
print(percentBdry)
sys.stdout.write(" \n")

#run again with 10 equal intervals
ntiles = 10
percentBdry = []
for i in range(ntiles+1):
    percentBdry.append(np.percentile(colArray, i*(100)/ntiles))
sys.stdout.write("Boundaries for 10 Eaual Percentiles \n")
print(percentBdry)
sys.stdout.write("\n")

#The last column contains categorical variables
col = 60
colData = []
for row in xList:
    colData.append(row[col])
unique = set(colData)
sys.stdout.write("Unique Label Values \n")
print(unique)
#count up the number of elements having each value
catDict = dict(zip(list(unique),range(len(unique))))
catCount = [0]*2
for elt in colData:
    catCount[catDict[elt]] += 1
sys.stdout.write("\nCounts for Each Value of Categorical Label \n")
print(list(unique))
print(catCount)