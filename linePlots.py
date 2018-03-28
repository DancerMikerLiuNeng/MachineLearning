_author__ = "sam zhang"
import requests
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases" \
             "/undocumented/connectionist-bench/sonar/sonar.all-data")


#read rocks versus mines data into pandas frame
rocksVMines = pd.read_csv(target_url, header=None, prefix="V")
for i in range(208):
    if rocksVMines.iat[i,60] == "M":
        pcolor = "red"
    else:
        pcolor = "blue"
    dataRow =  rocksVMines.iloc[i,0:60]
    dataRow.plot(color = pcolor)
plot.xlabel("Attribute Index")
plot.ylabel("Attribute Values")
plot.show()