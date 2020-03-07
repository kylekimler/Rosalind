import os.path
import sys
import time
from Bio import SeqIO

terminalinput1 = os.path.basename(sys.argv[1])

'''
def ParseSeqstoDict(filename):
	inputfasta=open(filename,'r')
	lines = inputfasta.readlines()
	z = str(lines[3][0])
	inputfasta.close()
	inputfasta = open(filename, 'r')
	if(z=='>'):
		stringmaker = [str(line.rstrip('\n').lstrip('>')) for line in inputfasta]
		parsedseqs = {stringmaker[x]: stringmaker[x+1] for x in range(0,len(stringmaker)-1,3)}
	elif(z!='>'):
		stringmaker = [str(line.rstrip('\n').lstrip('>')) for line in inputfasta]
		parsedseqs = {stringmaker[x]: stringmaker[x+1] for x in range(0,len(stringmaker)-1,2)}
	stringmaker = [str(line.rstrip('\n')) for line in inputfasta]
	inputfasta.close()
	return parsedseqs

ParseSeqsToDict cuts off fasta files at line breaks.... need to rewrite to allow!
So we are not using that function. I'll use a prepacked one instead, and
call it directly in the GC calculation function.
'''

def HighestGC(filename):
    highestGCid = ""
    highestGC = 0
    for record in SeqIO.parse(filename,"fasta"):
        GC = (record.seq.count('G')+record.seq.count('C'))/len(record.seq)*100
        if(GC>highestGC):
            highestGC=GC
            highestGCid=record.id

    print(highestGCid,"\n",highestGC)

HighestGC(terminalinput1)
