def magsom(u):
    zigma = 0
    for i in range(1, u+1):
        if u % i == 0:
            zigma += 1
    return zigma
lst = []
lst2 = []
lst3= []
for i in range(20):
    x = int(input())
    lst.append(x)
    lst2.append(magsom(x))
for i in lst:
    if magsom(i) == max(lst2):
        lst3.append(i)
print(max(lst3),'',max(lst2))