import os.path
import sys
import time
import math

terminalinput1 = os.path.basename(sys.argv[1])

with open(terminalinput1) as d:
    next(d)
    test = d.read().strip('\n').split(' ')
test2 = [int(i) for i in test]

#using the algorithm described on wikipedia originally created by Donald Knuth.
#This is by far the fastest method, but I can't figure out how to implement it
#for a decreasing subsequence.
def incsubsequence(seqlist):
    if not seqlist:
        return seqlist

    M = [None] * len(seqlist)
    P = [None] * len(seqlist)

    #this algorithm tracks longest increasing subsequences in a list by storing an increasing subsequence of all possible lengths
    #L is the length of the longest increasing subsequence found so far.
    #M[j] stores an index of seqlist that hold the first value in a subsequence of length j
    #Since we have at least one element in our list, we can start by
    #knowing that the there's at least an increasing subsequence of length one:
    #the first element, and M[0] points to that element.
    L = 1
    M[0] = 0

    #Next, we loop over the sequence starting from the second element,

    for i in range(1, len(seqlist)):
        #Binary search: we want the largest j <= L
        #such that seq[M[j]] < seq[i].
        #we want the lower bound at the end of the search process.
        lower = 0
        upper = L

        # Since the binary search will not look at the upper bound value,
        # we'll have to check that manually
        if seqlist[M[upper-1]] < seqlist[i]:
            j = upper

        else:
            #Now we perform a binary search for values smaller than the current one we are on.
            while upper - lower > 1:
                mid = (upper + lower) // 2
                if seqlist[M[mid-1]] < seqlist[i]:
                    lower = mid
                else:
                    upper = mid

            j = lower
        #set P[i] to the previous M. This way you can call back the subsequence
        #after you find the end, because P[x] will call M[j-x]
        P[i] = M[j-1]
        #
        if j == L or seqlist[i] < seqlist[M[j]]:
            M[j] = i
            L = max(L, j+1)

    #Rebuild the sequence: [seq[M[L-1]], seq[P[M[L-1]]], seq[P[P[M[L-1]]]], ...]
    result = []
    pos = M[L-1]
    #print(len(P))
    for _ in range(L):
        result.append(seqlist[pos])
        pos = P[pos]

    return result[::-1]    # reversing

print(*incsubsequence(test2))

#The shortest python solution,
def decreasingsubsequence(a):
	L = []
	for (k,v) in enumerate(a):
		L.append(max([L[i] for (i,n) in enumerate(a[:k]) if n>v] or [[]], key=len) + [v])
	return max(L, key=len)

print(*decreasingsubsequence(test2))
