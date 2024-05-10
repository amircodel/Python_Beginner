m = input()
t = input()
l = t.split()
l2 = []
for i in l:
    if i == '0' or i == '1' or i == '2' :
        l2.append(i)
r = (len(l2) // 3)
print(r)