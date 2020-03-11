import os.path
import sys
import time
import math
import itertools

terminalinput1 = os.path.basename(sys.argv[1])

with open(terminalinput1) as d:
    input = d.readlines()
    alphabet = input[0].strip('\n').replace(' ','')
    permlength = int(input[1])

def enumeratekmers(alphabet, length):
    kmers = []

    sortingdict = {b:a for a, b in enumerate(alphabet)}

    for i in range(1,length+1):
        kmerslist = [x for x in itertools.product(alphabet,repeat=i)]
        for bp in kmerslist:
            kmers.append(''.join([x for x in bp]))

    #kmers.sort(key=lambda i,j: alphabet.index(i))
    for kmer in kmers:
        print(kmer)
    print(sortingdict)

enumeratekmers(alphabet,permlength)
