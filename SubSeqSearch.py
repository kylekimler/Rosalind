import os.path
import sys
import time

terminalinput1 = os.path.basename(sys.argv[1])

def subseqsearch(filename):
    with open(filename, 'r') as d:
        lines=d.readlines()
        Searchedstr = lines[0].strip('\n')
        Searchstr = lines[1].strip('\n')
        searchbp = []
        subspots = []
        index=0
        for bp in Searchedstr:
            searchbp=Searchedstr[index:index+len(Searchstr)]
            if(Searchstr==searchbp):
                subspots.append(index)

            index+=1

        print(*subspots)


def subseqsearch1basenumbering(filename):
    with open(filename, 'r') as d:
        lines=d.readlines()
        Searchedstr = lines[0].strip('\n')
        Searchstr = lines[1].strip('\n')
        searchbp = []
        subspots = []
        index=0
        for bp in Searchedstr:
            searchbp=Searchedstr[index:index+len(Searchstr)]
            if(Searchstr==searchbp):
                subspots.append(index+1)

            index+=1

        print(*subspots)


subseqsearch1basenumbering(terminalinput1)
