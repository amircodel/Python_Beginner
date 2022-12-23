from collections import OrderedDict
l2 = []
d1 = OrderedDict()
n = int(input())
for i in range(n):
    l1 = []
    x = input()
    l1 = x.split()
    d1[l1[0]] = l1[1]
y = input()
l2 = y.split()
keyl1 = list(d1.keys())
valuel1 = list(d1.values())
for ch in l2 :
    if ch in keyl1 :
        l2[l2.index(ch)] = d1.get(ch)
resualt = ' '.join(l2).strip()
print(resualt)