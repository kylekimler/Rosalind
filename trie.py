import os.path
import sys
import time
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import statistics
import itertools

terminalinput1 = os.path.basename(sys.argv[1])

with open(terminalinput1) as d:
    read = d.readlines()

list = [x.strip('\n') for x in read]
list = sorted(list,key=len)[::-1]

list = [[x for x in string] for string in list]

triepos = 1

print(list)

trie = []

dna = list.pop(0)
i = 0
nextstarts = []
for bp in dna:
    triechar = bp
    trie.append([triepos,triepos+1,triechar])
    print([triepos,triepos+1,triechar])
    triepos+=1
    for string in list:
        try:
            if string[0] == triechar:
                del string[i]

            else:
                nextstarts.append(triepos)
        except:
            None
print(nextstarts)
print(list)
#dna = list.pop(0)

#need to work through by index, can only take the char away from
#other strings in list if it matches first AND FOLLOWING!
#same as the substring problem.
#
