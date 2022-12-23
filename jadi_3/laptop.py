n = int(input())
l1 = []
l2 = []
l3 = []
l4 = []
for i in range(n):
    x = input()
    l1 = x.split()
    l2.append(l1)
for i in l2 :
    p = int(i[0])
    q = int(i[1])
    l3.append(p)
    l4.append(q)
maxp = l3.index(max(l3))
for i in l4 :
    if int(l2[maxp][1]) < i :
        print('happy irsa')
        break
else:
        print('poor irsa')
