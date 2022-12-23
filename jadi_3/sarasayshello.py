x = input()
y = x
h = x.find('h')
x = x[h:]
e = x.find('e')
x = x[e:]
l1 = x.find('l')
x = x[l1+1:]
l2 = x.find('l')
x = x[l2:]
o = x.find('o')
if h >= 0 and e >= 0 and l1 >= 0 and l2 >= 0 and o >= 0 :
    print('YES')
elif h < 0 or e < 0 or l1 < 0 or l2 < 0 or o < 0 :
    print('NO')