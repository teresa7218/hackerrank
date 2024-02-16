#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'authEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY events as parameter.
#
import string 

M = 10**9 + 7
pp = [0] * 11
for i in range(11):
    pp[i] = 131**(i)
# can only append lowercase, uppercase, and digits
asciiappend = [""]+list(string.ascii_letters) + [str(d) for d in range(10)]
    
def authEvents(events):
    res = []
    
    
    
    def setPassword(s:str):
        for each in asciiappend:
            append = s + each
            i = 1
            n = len(append)
            h = 0
            
            for c in append:
                nmi = n-i
                h += ord(c)* (pp[nmi])
                i+=1
            hs = h % M
            goodhashes.add(hs)
        
    def authorize(x:int):
        
        if x in goodhashes:
            res.append(1)
        else:
            res.append(0)
            
                 
    for event in events:
        if event[0] == "setPassword":
            goodhashes = set()
            setPassword(event[1])
        elif event[0] == "authorize":
            authorize(int(event[1]))
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    events_rows = int(input().strip())
    events_columns = int(input().strip())

    events = []

    for _ in range(events_rows):
        events.append(input().rstrip().split())

    result = authEvents(events)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
