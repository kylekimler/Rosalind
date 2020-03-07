import os.path
import sys
import time

DNAstring = os.path.basename(sys.argv[1])

ComplementDict = {
'A':'T',
'C':'G',
'T':'A',
'G':'C'
}

def Complement_ACGT(filename):
  with open(filename, 'r') as d:
    DNAstr = d.read().strip('\n')
    compbp = []
    for bp in DNAstr:
        compbp.append(ComplementDict[bp])
    print("".join(compbp)[::-1])

Complement_ACGT(DNAstring)
