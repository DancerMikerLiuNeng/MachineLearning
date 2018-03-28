__author__ = 'sam zhang'
import requests
import sys

target_url = "http://archive.ics.uci.edu/ml/machine-learning-databases" \
             "/undocumented/connectionist-bench/sonar/sonar.all-data"
ret = requests.get(target_url)
data = ret.text
# print(type(data))
xList = []
labels = []

for line in data.split("\n"):
    row = line.strip().split(",")
    if len(row)>1:
        xList.append(row)
sys.stdout.write("Number of rows of Data = "+ str(len(xList)) + '\n')
sys.stdout.write("Number of Columns of Data = "+ str(len(xList[1])))
