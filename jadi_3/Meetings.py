def masafat(u, z):
    resualt = abs(u-z)
    return resualt
x = input()
x = x.split()
list=[]
list.append(masafat(float(x[0]),float(x[1])))
list.append(masafat(float(x[1]),float(x[2])))
list.append(masafat(float(x[0]),float(x[2])))
answer = max(list)
if int(answer) == answer :
    print(int(answer))
else:
    print(answer)