x = int(input())
x3 = str(x % 10)
x2 = str((x // 10) % 10)
x1 = str((x // 100) % 10)
print((int(x3 + x2 + x1) * 2))