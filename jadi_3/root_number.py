from collections import OrderedDict
l1 = []
def ray(con) :
    dicc = OrderedDict()
    for c in con :
        counter = con.count(c)
        dicc[c] = counter
    dicc = OrderedDict(sorted(dicc.items(), key = lambda x: x[0], reverse= False))
    return dicc
n = int(input())
for i in range(n) :
    x = input()
    l1.append(x)
for k,v in ray(l1).items() :
    print(k,'',v)