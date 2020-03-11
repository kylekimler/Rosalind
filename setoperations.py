import os.path
import sys
import time
import math

terminalinput1 = os.path.basename(sys.argv[1])

with open(terminalinput1) as d:
    input = d.readlines()
    setA = input[1].strip('\n').strip('{}').split(', ')
    setA = set([int(i) for i in setA])
    setB = input[2].strip('\n').strip('{}').split(', ')
    setB = set([int(i) for i in setB])

union= setA.union(setB)
print(union)
fullset = set([i for i in range(1,int(input[0])+1)])
print(setA.intersection(setB))
print(setA.difference(setB))
print(setB.difference(setA))
print(fullset.difference(setA))
print(fullset.difference(setB))
