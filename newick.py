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

treelist = list[::3]
nodeslist = list[1::3]

tree1 = treelist[0]
tree2 = treelist[1]

import io
from Bio import Phylo

distancelist = []
distancelist0 = []

for i in range(len(treelist)):
    handle = io.StringIO(treelist[i])
    tree = Phylo.read(handle, 'newick')

    nodes = nodeslist[i].split(' ')
    distance = 0
    #clades = tree.find_clades()
    #for clade in clades:
    #    clade.branch_length = 1
    distancelist0.append(int(tree.distance(nodes[0],nodes[1])))

    ''' the trace method with counting clades does not work, but only in some cases.
    I don't fully understand newick format.
    distancemap = tree.trace(nodes[0],nodes[1])

    x = False
    for j in distancemap:
        distance+=1
        if j.name==None:
            x = True
    if x == False:
        distance-=1
    distancelist.append(distance)
    '''

print(*distancelist0)
#print(*distancelist)

#handle = io.StringIO(tree1)
#tree = Phylo.read(handle, 'newick')
#tree.rooted = True
#print(tree)
#print(tree.distance('dog','cat'))
#Phylo.draw(tree)
#print(test)
#print(tree)
#Phylo.draw_ascii(tree)
#print(test.distance('dog','cat'))
#print(tree)
#Phylo.draw_ascii(tree)
#pylab.show()
