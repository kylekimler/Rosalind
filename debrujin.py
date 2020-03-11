import os.path
import sys
import time
import math
import itertools
from Bio import SeqIO

terminalinput1 = os.path.basename(sys.argv[1])

with open(terminalinput1) as d:
    kmers = d.readlines()
    kmers = [kmer.strip('\n') for kmer in kmers]

#print(kmers)

dbjk = len(kmers[0])-1

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

def UnionS(kmers):
    UnionS = []
    for kmer in kmers:
        UnionS.append(kmer)
        UnionS.append(Complement_ACGT(kmer))
    return set(UnionS)

def debrujin(kmerunion):
    debrujin = []
    for kmer in kmerunion:
        debrujin.append([kmer[0:dbjk],kmer[len(kmer)-dbjk:len(kmer)]])
    for edge in debrujin:
        print(str(edge).replace('[','(').replace(']',')').replace("'",""))
    return debrujin

kmerunion = UnionS(kmers)
#print(kmerunion)

debrujin(kmerunion)
