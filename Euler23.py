#Euler23
import time
start_time = time.time()
cap = 100

#checking abundant numbers
def isAbund(n):
    divs = set()
    divsum = sum([div for div in range(1,n) if n%div == 0])
    return(divsum>n)

abund = []
for i in range(cap):
    if isAbund(i):
        abund.append(i)

#binary search
def binsearch(list, item):
    hi = len(list)-1
    lo = 0
    found = False
    while lo<=hi and not found:
        mid = (hi+lo)//2
        if list[mid] == item:
            found = True
        else:
            if item < list[mid]:
                hi = mid-1
            else:
                lo = mid+1
    return True


#getting nums which cant be sum omf abund numbers
testcap = 100
for n in range(testcap):
    for i in range(n):
        a = abund[i]
        for j in range(n):
            if n == j+i:
                validnr = False
                break
    if validnr:
        sum+=n

print(abund)
print("--- %s seconds ---" % (time.time()-start_time))
