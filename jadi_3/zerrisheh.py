x = input().upper()
y = x.replace("AB" , "@" , 1)
z = y.replace("BA" , "&")
if "@" in z and "&" in z :
    print('YES')
else:
    print('NO')