'''
Created on 2017/04/16

@author: smallcat
'''

# traffic pattern 

import pandas as pd

traffic_pattern = "uniform"  #uniform, reversal, matrix, neighbor, shuffle, butterfly, complement, tornado, alltoall
degree = 5
nodes = 1024  #number of nodes
MS = 14

archive = "result_mkpkt-huyao/" + traffic_pattern + "-" + str(nodes) + "-trim2.txt"

names = ["src", 
         "dst"]

data = pd.read_csv(archive, comment=";", sep="\s+", names=names)