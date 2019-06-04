#euler 18
f = open("euler18input.txt", "r")
a = []
for i in range(15):
	f1 = f.readline().split()
	f2 = [int(i) for i in f1]
	a.append(f1)

print(a)
