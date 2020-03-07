import os.path
import sys
import time
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


terminalinput1 = os.path.basename(sys.argv[1])

def PrefixSuffix(inputfasta,k):
    preflist=[]
    suflist=[]

    with open(inputfasta, 'r') as d:
        fa_dict=SeqIO.index(inputfasta,"fasta")

        for record in SeqIO.parse(d,"fasta"):

            prefix = record.seq[0:k]
            prefixRecord =SeqRecord(prefix,record.id,'','')
            preflist.append(prefixRecord)

            suffix = record.seq[-k:]
            suffixRecord = SeqRecord(suffix,record.id,'','')
            suflist.append(suffixRecord)

        SeqIO.write(preflist, "preflist.fasta","fasta")
        SeqIO.write(suflist, "suflist.fasta","fasta")

def DiGraph(suflist, preflist):

    DiGraph=[]
    for prefix in SeqIO.parse(preflist,"fasta"):
        for suffix in SeqIO.parse(suflist,"fasta"):
            if prefix.seq == suffix.seq and prefix.id != suffix.id:
                DiGraph.append([prefix.id,suffix.id])
    print(*DiGraph,sep="\n")
'''
your substring search method
        lines=d.readlines()
        Searchedstr = lines[0].strip('\n')
        Searchstr = lines[1].strip('\n')
        searchbp = []
        subspots = []
        index=0
        for bp in Searchedstr:
            searchbp=Searchedstr[index:index+len(Searchstr)]
            if(Searchstr==searchbp):
                subspots.append(index)

            index+=1
'''

PrefixSuffix(terminalinput1,3)
DiGraph("preflist.fasta","suflist.fasta")
