import os.path
import sys
import time
import math
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

seqaslist = [bp for bp in seqs[0]]
seqstr = seqs[0]
introns = [i for i in seqs[1:]]
intron1 = seqs[1]
intron2 = seqs[2]

def splice(seqaslist, seqstr, introns):
    for i in introns:
        spliceloci = subseqsearch(seqstr,i)
        #reverse loci so deletion doesn't ruin indices
        for j in reversed(sorted(spliceloci)):
            del seqaslist[j:j+len(i)]
        seqstr = ''.join(seqaslist)
        #set the new seqstr to delete
    return ''.join(seqaslist)


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

splicedseq = splice(seqaslist,seqstr, introns)

TranslateDict = {
"UUU" : "F",
"CUU" : "L",
"AUU" : "I",
"GUU" : "V",
"UUC" : "F",
"CUC" : "L",
"AUC" : "I",
"GUC" : "V",
"UUA" : "L",
"CUA" : "L",
"AUA" : "I",
"GUA" : "V",
"UUG" : "L",
"CUG" : "L",
"AUG" : "M",
"GUG" : "V",
"UCU" : "S",
"CCU" : "P",
"ACU" : "T",
"GCU" : "A",
"UCC" : "S",
"CCC" : "P",
"ACC" : "T",
"GCC" : "A",
"UCA" : "S",
"CCA" : "P",
"ACA" : "T",
"GCA" : "A",
"UCG" : "S",
"CCG" : "P",
"ACG" : "T",
"GCG" : "A",
"UAU" : "Y",
"CAU" : "H",
"AAU" : "N",
"GAU" : "D",
"UAC" : "Y",
"CAC" : "H",
"AAC" : "N",
"GAC" : "D",
"UAA" : "stop",
"CAA" : "Q",
"AAA" : "K",
"GAA" : "E",
"UAG" : "stop",
"CAG" : "Q",
"AAG" : "K",
"GAG" : "E",
"UGU" : "C",
"CGU" : "R",
"AGU" : "S",
"GGU" : "G",
"UGC" : "C",
"CGC" : "R",
"AGC" : "S",
"GGC" : "G",
"UGA" : "stop",
"CGA" : "R",
"AGA" : "R",
"GGA" : "G",
"UGG" : "W",
"CGG" : "R",
"AGG" : "R",
"GGG" : "G"
}

def Translate(RNAstring):
    p = [TranslateDict[RNAstring[x:x+3]] for x in range(0,len(RNAstring),3)]
    return ''.join(p)

TranscribeDict = {
'A':'A',
'C':'C',
'T':'U',
'G':'G'
}

def Transcribe(DNAstring):
    txnbp = []
    for bp in DNAstring:
        txnbp.append(TranscribeDict[bp])
    return ''.join(txnbp)

print(Translate(Transcribe(splicedseq)))
