x = int(input())
mod = x % 10
if mod != 0 :
    x -= mod
print(x + 10)