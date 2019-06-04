#project euler problem 12 

import math
a = 100
divs = 0

def trinum(n):
    if n == 0:
        return 0
    else:
        return n + trinum(n - 1)

while(divs<100):
    divs = 0
    for i in range(1, math.ceil(trinum(a)/2)):
        if trinum(a)%i == 0:
            divs += 1
    a += 1

print (trinum(a-2))
print ("end")
