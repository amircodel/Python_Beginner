import math
x = int(input())
l1 = []
for i in range(x):
    y = float(input())
    r = math.sqrt(y)
    f = math.floor(r*10000)/10000
    l1.append("%.4f" % f)
for l in l1 :
    print(l)