#Euler23
import time
start_time = time.time()
def isAbund(n):
    divs = set()
    divsum = sum([div for div in range(1,n) if n%div == 0])
    return(divsum>n)

cap1 = 28123
abund = []
for i in range(cap1):
    if isAbund(i):
        abund.append(i)

'''
for n in range(20):
    validnr = True
    for i in abund:
        for j in abund:
            if n == j+i:
                validnr = False
                break
    if validnr:
        sum+=n
'''
print(abund)
print("--- %s seconds ---" % (time.time()-start_time))
