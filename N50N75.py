import os.path
import sys
import statistics
import math
import numpy as np

terminalinput1 = os.path.basename(sys.argv[1])

with open(terminalinput1) as d:
    reads = d.readlines()
    reads = [read.strip('\n') for read in reads]

lengths = sorted([len(contig) for contig in reads])

def n50(lengths):
    count=0
    a = sum(lengths)
    n50sum = 0.5 * a
    i = len(lengths)-1
    while count < n50sum:
        count += lengths[i]
        i = i - 1
    return lengths[i]

def n75(lengths):
    count=0
    a = sum(lengths)
    n75sum = 0.75 * a
    i = len(lengths)-1
    while count < n75sum:
        count += lengths[i]
        i = i - 1
    return lengths[i]
    print(a)


print(n50(lengths),n75(lengths))
