import os.path
import sys
import time
import math

terminalinput1 = os.path.basename(sys.argv[1])

with open(terminalinput1) as d:
    num = d.read().strip('\n')

def numsubsets(number):
    return 2**int(number) % 1000000

print(numsubsets(num))
