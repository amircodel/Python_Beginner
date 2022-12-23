x = input().replace('+' , '')
x1 = ''
x2 = ''
x3 = ''
for n in x :
    if n == '1' :
        x1 += '+1'
    elif n == '2' :
        x2 += '+2'
    elif n == '3' :
        x3 += '+3'
result = (x1 + x2 + x3).strip('+')
print(result)