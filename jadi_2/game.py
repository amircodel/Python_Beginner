import random
mini = 1
maxi = 99
hads = random.randint(mini, maxi)
print(hads)
j = input().upper()
while j != 'D':
    if j == 'K':
        maxi = hads
        hads = random.randint(mini, maxi)
        print(hads)
        j = input().upper()
    elif j == 'B' :
        mini = hads + 1
        hads = random.randint(mini, maxi)
        print(hads)
        j = input().upper()
print("gg!")