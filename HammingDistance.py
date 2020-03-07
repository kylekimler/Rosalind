import os.path
import sys
import time
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


terminalinput1 = os.path.basename(sys.argv[1])

with open(terminalinput1, 'r') as d:
    DNA = d.readlines()
    DNA1 = DNA[0].rstrip('\n')
    DNA2 = DNA[1].rstrip('\n')
    count=0
    for x in range(len(DNA1)):
        if DNA1[x]!=DNA2[x]:
            count+=1
    print(count)


def HamDistance(seq1,seq2):
    count = sum(1 for a, b in zip(seq1,seq2) if a!=b)
    return count
