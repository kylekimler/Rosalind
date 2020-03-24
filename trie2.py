import os.path
import sys
import time
import pygtrie
import collections

terminalinput1 = os.path.basename(sys.argv[1])

with open(terminalinput1) as d:
    read = d.readlines()

#Parse sequences into string list
list = [x.strip('\n') for x in read]
list = sorted(list,key=len)[::-1]
#or for tuple of character lists
#set = set([x for x in string for string in list])

test = pygtrie.Trie.fromkeys(list)
print(test)

for k in list:
    for n in k:
        print(test.prefixes(n))
