import os.path
import sys
import time
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import statistics


terminalinput1 = os.path.basename(sys.argv[1])

def ParseSeqstoList(inputfasta):
    Seqlist=[]
    idlist=[]

    with open(inputfasta, 'r') as d:
        for record in SeqIO.parse(d,"fasta"):
            Seqlist.append(str(record.seq))
            idlist.append(record.id)
    return Seqlist

seqslist = ParseSeqstoList(terminalinput1)


#Method using overlap graph and substring finding algorithms from previous exercises

sizes = [len(rec) for rec in SeqIO.parse(terminalinput1, "fasta")]
k = int(statistics.mean(sizes)/2)


def Overlap(seq1,seq2):
    overlap = []
    z=0
    #loop through the first sequence
    for x in range(len(seq1)):
        #loop through second sequence
        for y in range(len(seq2)):
            #check for nucleotide match
            if seq1[x] == seq2[y]:
                overlap.append(seq1[x])
                yy=y+1
                #if a match is found, check if next nucleotides match
                for z in range(x+1,len(seq1)):
                    if seq1[z] == seq2[yy]:
                        #if so, add to the overlap
                        overlap.append(seq1[z])
                        yy+=1
                    else:
                        #if the overlap has stopped before the end, clear it.
                        overlap =[]
                        break
                break
            if seq1[x] != seq2[y]:
                break
        #if the sequential match position reached the end of seq1, break.
        if z == len(seq1)-1:
            break
    return ''.join(overlap)

def SuffixOverlap(seq1,seq2):
    overlap = []
    pre =[]
    z=0
    #loop through the first sequence
    for x in range(len(seq1)):
        #Store the sequence before an overlap is found
        pre.append(seq1[x])
        #loop through second sequence
        for y in range(len(seq2)):
            #check for nucleotide match

            if seq1[x] == seq2[y]:
                overlap.append(seq1[x])
                yy=y+1
                #if a match is found, check if next nucleotides match
                for z in range(x+1,len(seq1)):
                    if seq1[z] == seq2[yy]:
                        #if so, add to the overlap
                        overlap.append(seq1[z])
                        yy+=1
                    else:
                        #if the overlap has stopped before the end, clear it.
                        overlap =[]
                        break
                break
            if seq1[x] != seq2[y]:
                break
        #if the sequential match position reached the end of seq1, break.
        if z == len(seq1)-1:
            #remove the nucleotide where the match started from the prepend list
            del pre[-1]
            #For suffix overlapping, add the pre-overlap of seq1

            if ''.join(overlap) == seq2:
                overlap=pre+overlap
                break
            overlap=pre+overlap
            #For Suffix Overlapping, add the remainder of both sequences to
            #the overlap.
            rest = [seq2[yy] for yy in range(yy,len(seq2))]
            overlap+=rest
            break
    return ''.join(overlap)

#print("testing overlap function:", Overlap(seqslist[0],seqslist[1]))
#print("testing soverlap function:", SuffixOverlap(seqslist[0],seqslist[1]))

def Combo(Seqslist, overlapsize):
    while len(Seqslist) != 1:
        #print(Seqslist)
        for y in range(1,len(Seqslist)):
            #print("loop2pos: ",y)
            #conditions for allowing an overlap:
            if len(Overlap(Seqslist[0],Seqslist[y])) > overlapsize:
            #    print("found a good overlap! Between sequences :", Seqslist[0],Seqslist[y])

            #    print("good overlap:",SuffixOverlap(Seqslist[0],Seqslist[y]))
                Seqslist.append(SuffixOverlap(Seqslist[0],Seqslist[y]))
            #    print("appended list with new overlap:",Seqslist)
            #    print("removing sequences:",Seqslist[0],Seqslist[y])
                del Seqslist[y]
                del Seqslist[0]
            #    print("remaining list:",Seqslist)
                break
            #print("length of seqsList: ",len(Seqslist))
            if y == len(Seqslist)-1:
                Seqslist.insert(0,Seqslist.pop())

    return(Seqslist)

print(*Combo(seqslist, k))

#def shortestCommon(Seqslist):



#This method lines up ALL POSSIBLE permutations of the given dataset and finds
#the best shortest superstring by hooking them together indiscriminately
#But there are too many possibilities in datasets of over 10 reads!

'''
def ParseFastaForPermutation(inputfasta):
    Seqlist=[]
    idlist=[]

    with open(inputfasta, 'r') as d:
        for record in SeqIO.parse(d,"fasta"):
            Seqlist.append(str(record.seq))
            idlist.append(record.id)
    return Seqlist

seqslist = ParseFastaForPermutation(terminalinput1)


def overlap(a, b):
    """ Return length of longest suffix of 'a' matching a prefix of 'b' that
        covers at least half of the prefix containing string.  If no such
        overlap exists, return 0. """

    start = 0  # start all the way at the left
    while True:
        min_length = int(len(b)/2)+1
        start = a.find(b[:min_length], start)  # look for b's suffix in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += min_length  # move just past previous match

def SuperStringer(Seqlist):
    import itertools
    shortest_superstring=[]
    shortest_len=0
    #print(sum(1 for ignore in itertools.permutations(Seqlist)))
    z=0
    for recordpermutation in itertools.permutations(Seqlist):
        #the superstring starts as the first string in the list
        print(z)
        superstring = recordpermutation[0]
        for x in range(len(Seqlist)-1):
            # overlap adjacent strings in this permutation
            randomlyoverlap = overlap(recordpermutation[x],recordpermutation[x+1])
            # conglomerate the end of matching string to the superstring
            superstring += recordpermutation[x+1][randomlyoverlap:]
        if shortest_len == 0:
            shortest_superstring.append(superstring)
            shortest_len = len(superstring)
        elif len(superstring) < shortest_len:
            shortest_len = len(superstring)
            shortest_superstring = [superstring]
        elif len(superstring) == shortest_len:
            shortest_superstring.append(superstring)
        else:
            None
        z+=1
    return sorted(shortest_superstring)

print(*SuperStringer(seqslist))
'''
