import os.path
import sys
import time
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import statistics
import itertools

terminalinput1 = os.path.basename(sys.argv[1])

with open(terminalinput1) as d:
    num = d.read().strip('\n').split(' ')
    n = int(num[0])
    k = int(num[1])

def NumPartialPermutations(n,k):
    num = 1
    for i in range(n, n-k, -1):
        num *= i
    return num%1000000

print(NumPartialPermutations(n,k))
