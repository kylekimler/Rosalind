import os.path
import sys
import time
import math
import itertools

terminalinput1 = os.path.basename(sys.argv[1])

with open(terminalinput1) as d:
    kmers = d.readlines()
    kmers = [kmer.strip('\n') for kmer in kmers]

print(kmers)
dbjk = len(kmers[0])-1

def debrujin(kmerunion):
    debrujin = []
    for kmer in kmerunion:
        debrujin.append([kmer[0:dbjk],kmer[len(kmer)-dbjk:len(kmer)]])
    return debrujin

print(debrujin(kmers))

def dbjassembly(dbjgraph):
    assembly = dbjgraph[0][0]
    while len(assembly) < len(kmers):
        for connection in dbjgraph:
            #print(assembly[0][-dbjk])
            if connection[0] == assembly[-dbjk:]:
                assembly+=connection[1][-1]
                print(assembly)
                if len(assembly) >= len(kmers):
                    break
    return assembly

print(dbjassembly(debrujin(kmers)))
