import os.path
import sys
import time
import math
import random
import itertools
from itertools import chain
from collections import defaultdict
from collections import Counter

terminalinput1 = os.path.basename(sys.argv[1])

with open(terminalinput1) as d:
    reads = d.readlines()
    reads = [read.strip('\n') for read in reads]

dbjk = len(reads[0])-1

def debrujin(kmerunion):
    debrujin = []
    for kmer in kmerunion:
        for bp in range(len(kmer)-dbjk):
            debrujin.append([kmer[bp:bp+dbjk],kmer[bp+1:bp+dbjk+1]])
    return debrujin

def debrujindict(kmers):
    tupletodict = lambda tuple: chain.from_iterable(tuple)
    dbjdict = dict(tupletodict([[(kmer[i:i+dbjk], kmer[i+1:i+dbjk+1]) for i in range(len(reads[0])-dbjk)] for kmer in kmers]))
    return dbjdict

def debrujindefdict(kmers):
    dbjdict = defaultdict(list)
    for i,k in debrujin(kmers):
        dbjdict[i].append(k)
    return dbjdict

FullDictionary = debrujindefdict(reads)
Targets = [x for x,y in FullDictionary.items() for x in y]
PossibleAssemblies = len(Targets)-len(set(Targets))

def dbjassembly5():
    setofassemblies = set()
    deadendcount = 0
    z = time.time()
    test = 0
    #while len(setofassemblies) < PossibleAssemblies:
    while test < 10:
        firsttime = True
        dbjgraph = debrujindefdict(reads)
        assembly = ''
        first = connection = next(iter(dbjgraph))
        kmerlength = len(first)-1
        assembly += connection[-1]
        try:
            while True:
                if firsttime==True:
                    key = connection
                    connection = reads[0][-2:]
                    choice = 0
                    listinstance = list(dbjgraph[key])
                    del dbjgraph[first]
                    firsttime=False
                else:
                    listinstance = list(connection)
                    choice = random.choice(range(len(connection)))
                    connection = connection[choice]

                del listinstance[choice]

                for k in listinstance:
                    dbjgraph[key].append(k)

                if len(assembly) == len(reads):
                    assembly = assembly[-1] + assembly[:-1]
                    setofassemblies.add(assembly)
                    break

                assembly+=connection[-1]
                key = connection
                connection = dbjgraph.pop(connection)
        except:
            print(assembly)
            deadendcount+=1
        test = time.time()-z
        print(test)
    print("dead end count:",deadendcount)
    for i in setofassemblies:
        print(i)
    return setofassemblies

def dbjassembly6():
    setofassemblies = set()
    deadendcount = 0
    z = time.time()
    test = 0
    while test < 3:
        firsttime = True
        dbjgraph = debrujindefdict(reads)
        assembly = ''
        first = connection = next(iter(dbjgraph))
        kmerlength = len(first)
        assembly += connection[1:]
        try:
            while True:
                if firsttime==True:
                    key = connection
                    connection = reads[0][-kmerlength:]
                    choice = 0
                    listinstance = list(dbjgraph[key])
                    del dbjgraph[first]
                    firsttime=False
                else:
                    listinstance = list(connection)
                    choice = random.choice(range(len(connection)))
                    connection = connection[choice]

                del listinstance[choice]

                for k in listinstance:
                    dbjgraph[key].append(k)

                if len(assembly) == len(reads)+1 and connection == first:
                    assembly = assembly[-2] + assembly[:-kmerlength+1]
                    setofassemblies.add(assembly)
                    #print(setofassemblies)
                    break

                assembly+=connection[-1]
                key = connection
                connection = dbjgraph.pop(connection)
        except:
            deadendcount+=1
        test = time.time()-z
    #print("dead end count:",deadendcount)
    for i in setofassemblies:
        print(i)
    return setofassemblies

dbjassembly6()
