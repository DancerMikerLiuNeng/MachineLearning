__author__ = "sam zhang"
import requests
import sys
import numpy as np
import pylab
import scipy.stats as stats


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

#generate summary statistics for column 3 (e.g)
col = 3
colData = []
for row in xList:
    colData.append(float(row[col]))
print(colData)
stats.probplot(colData, dist="norm", plot=pylab)
pylab.show()