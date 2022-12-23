zigmay = 0
def zigma(u):
    global zigmay
    if u == 3 :
        zigmay += 1
x = int(input())
y = int(input())
zigma(x)
zigma(y)
for i in range(28):
    x = x + y
    y = int(input())
    ssum = x + y
    zigma(y)
print(ssum,'',zigmay)