import os.path
import sys
import time
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import itertools

terminalinput1 = os.path.basename(sys.argv[1])

with open(terminalinput1) as d:
    pop = d.read().strip('\n').split()


totalpop = sum(int(x) for x in pop)

homo = int(pop[0])
hetero = int(pop[1])
homo2 = int(pop[2])

population = (['KK']*homo) + (['Kk']*hetero) + (['kk']*homo2)

PhenoDict = {
'KK':'Dominant',
'Kk':'Hetero',
'kK':'Hetero2',
'kk':'Recessive'
}

children = []

def recombine(a,b):
    children = []
    for allele in a:
        child = allele
        for allele2 in b:
            child += allele2
            children.append(child)
            child = allele
    return children

childcount = 0
PossibleChildren = []
for parent in population:
    otherpops = population
    otherpops.remove(parent)
    for otherparent in population:
        children = recombine(parent,otherparent)
        PossibleChildren+=children
        childcount+=len(children)

probabilities = []
for key in PhenoDict:
    num = sum(1 for value in PossibleChildren if value==key)/childcount
    probabilities.append(num)
    print('Phenotype children: ',PhenoDict[key],num)

Dominant = sum(probabilities[0:3])
print('total with dominant trait',Dominant)
Recessibe = probabilities[3]
print('total with recessive trait',Recessibe)
