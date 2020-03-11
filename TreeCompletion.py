import os.path
import sys
import time
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import statistics


terminalinput1 = os.path.basename(sys.argv[1])



def parseAdjacency(adjfile):
    with open(adjfile) as d:
        x = d.readlines()
        y=[]
        for z in x:
            y.append(z.strip('\n').split(' '))
        print(y)
    TreeSize = y[0]
    TreeSize = int(TreeSize[0])
    del y[0]
    Edges = TreeSize-1
    print(len(y))
    print(Edges)
    minEdgesNeeded = Edges-len(y)
    print(minEdgesNeeded)

parseAdjacency(terminalinput1)
