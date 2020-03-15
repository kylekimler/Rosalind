import os.path
import sys
import time
import math
import itertools
from itertools import chain

terminalinput1 = os.path.basename(sys.argv[1])

with open(terminalinput1) as d:
    reads = d.readlines()
    reads = [read.strip('\n') for read in reads]

dbjk = int(os.path.basename(sys.argv[2]))

ComplementDict = {
'A':'T',
'C':'G',
'T':'A',
'G':'C'
}

def Complement_ACGT(DNA):
    compbp = []
    for base in DNA:
        compbp.append(ComplementDict[base])
    return "".join(compbp)[::-1]



def UnionK(kmers):
    UnionK = []
    for kmer in kmers:
        UnionK.append(kmer)
        UnionK.append(Complement_ACGT(kmer))
    return set(UnionK)

def debrujin(kmerunion):
    debrujin = []
    for kmer in kmerunion:
        for bp in range(len(kmer)-dbjk):
            debrujin.append([kmer[bp:bp+dbjk],kmer[bp+1:bp+dbjk+1]])
    return debrujin

def debrujindict(kmerunion):
    tupletodict = lambda tuple: chain.from_iterable(tuple)
    dbjdict = dict(tupletodict([[(kmer[i:i+dbjk], kmer[i+1:i+dbjk+1]) for i in range(len(reads[0])-dbjk)] for kmer in kmerunion]))
    return dbjdict

dbj = debrujindict(UnionK(reads))

def dbjassembly(dbjgraph, k):
    assembly = dbjgraph[0][0]
    dbjgraph.remove(dbjgraph[0])
    end = len(dbjgraph)
    test = 0
    while len(assembly) < end/2-1:
        for connection in dbjgraph:
            #print(assembly[0][-dbjk])
            if connection[0] == assembly[-dbjk:]:
                assembly+=connection[1][-1]
                dbjgraph.remove(connection)
                #print(assembly)
                if len(assembly) >= end/2:
                    break
        test+=1
        if test == 2000:
            break
    return assembly

def dbjassembly2(dbjgraph):
    assembly = ''
    connection = next(iter(dbjgraph))
    firstconnection = connection
    #print(connection)
    #print(assembly[0][-dbjk])
    while True:
        if connection in dbjgraph:
            assembly+=connection[-1]
            connection = dbjgraph.pop(connection)
            if connection == firstconnection:
                return assembly
        else:
            break


        #print(assembly)

    '''
    assembly2 = dbjgraph[0][0]
    dbjgraph.remove(dbjgraph[0])
    end = len(dbjgraph)
    print(dbjgraph)
    while len(assembly) < end/2-1:
        for connection in dbjgraph:
            #print(assembly[0][-dbjk])
            if connection[0] == assembly2[-dbjk:]:
                assembly2+=connection[1][-1]
                dbjgraph.remove(connection)
                #print(assembly)
                if len(assembly2) > end/2:
                    break
    print(len(assembly2) is len(assembly))
    print(assembly2)
    '''


#print(dbj)
print(dbjassembly2(dbj))
#print(dbjassembly(sorted(dbj),dbjk))
