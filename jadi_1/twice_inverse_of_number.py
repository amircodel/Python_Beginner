x0 = int(input())
x1 = str(x0 % 10)
x2 = str((x0 // 10) % 10)
x3 = str((x0 // 100) % 10)
print((int(x1 + x2 + x3) * 2))