x = int(input())
lst = []
while x >= 0 :
    lst.append(x)
    x = int(input())
maxi = lst.pop(lst.index(max(lst)))
print(maxi, '', max(lst))