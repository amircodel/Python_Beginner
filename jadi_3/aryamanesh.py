lower = 0
upper = 0
x = input()
for ch in x :
    if ch.islower():
        lower += 1
    else: 
        upper += 1
if lower >= upper :
    x = x.lower()
else:
    x = x.upper()
print(x)