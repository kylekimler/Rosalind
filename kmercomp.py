import os.path
import sys
import time
import math
import itertools
from Bio import SeqIO

terminalinput1 = os.path.basename(sys.argv[1])

def ParseSeqstoList(inputfasta):
    Seqlist=[]
    idlist=[]

    with open(inputfasta, 'r') as d:
        for record in SeqIO.parse(d,"fasta"):
            Seqlist.append(str(record.seq))
            idlist.append(record.id)
    return Seqlist

seqs = ParseSeqstoList(terminalinput1)

def enumeratekmers(alphabet, length):
    kmers = []

    sortingdict = {b:a for a, b in enumerate(alphabet)}

    kmerslist = [x for x in itertools.product(alphabet,repeat=length)]
    for bp in kmerslist:
        kmers.append(''.join([x for x in bp]))

    #kmers.sort(key=lambda i,j: alphabet.index(i))
    return(kmers)
    #print(sortingdict)

def subseqsearch(Searchedstr,Searchstr):
    searchbp = []
    subspots = []
    index=0
    for bp in Searchedstr:
        searchbp=Searchedstr[index:index+len(Searchstr)]
        if(Searchstr==searchbp):
            subspots.append(index)

        index+=1

    return subspots

def kmercomp(kmers, seq):
    comp = []
    for kmer in kmers:
        count = len(subseqsearch(seq,kmer))
        comp.append(count)
    return comp


alphabet = ['A','C','G','T']

kmers=enumeratekmers(alphabet, 4)
print(*kmercomp(kmers,seqs[0]))
