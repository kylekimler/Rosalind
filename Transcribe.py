import os.path
import sys
import time

DNAstring = os.path.basename(sys.argv[1])

TranscribeDict = {
'A':'A',
'C':'C',
'T':'U',
'G':'G'
}

def Transcribe_ACGT(filename):
  with open(filename, 'r') as d:
    DNAstr = d.read().strip('\n')
    txnbp = []
    for bp in DNAstr:
        txnbp.append(TranscribeDict[bp])
    print("".join(txnbp))

Transcribe_ACGT(DNAstring)
