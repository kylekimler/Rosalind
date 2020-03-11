import os.path
import sys
import time
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import statistics
import itertools

terminalinput1 = os.path.basename(sys.argv[1])

with open(terminalinput1) as d:
    num = int(d.read())

def Permutations(num):
    enumerate = [x+1 for x in range(num)]
    permutations = itertools.permutations(enumerate)
    print(len(list(permutations)))
    for z in itertools.permutations(enumerate):
        printlist=[]
        for zz in z:
            printlist.append(zz)
        print(*printlist)
    #print(*(list(permutations)),sep='\n')
    #return len(permutations)
    #print(*permutations)

print(Permutations(num))
