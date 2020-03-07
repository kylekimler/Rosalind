import os.path
import sys
import time

DNAstring = os.path.basename(sys.argv[1])

def count_ACGT(filename):
  with open(filename, 'r') as d:
    DNAstr = d.read()
    A = DNAstr.count('A')
    C = DNAstr.count('C')
    G = DNAstr.count('G')
    T = DNAstr.count('T')
    print(A,C,G,T)
 # C = DNAstring.count('C')
  #G = DNAstring.count('G')
  #T = DNAstring.count('T')
  return
count_ACGT(DNAstring)
