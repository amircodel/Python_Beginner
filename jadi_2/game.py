import random
mini = 1
maxi = 99
hads = random.randint(mini, maxi)
print(hads)
j = input()
while j != 'd':
    if j == 'k':
        maxi = hads
        hads = random.randint(mini + 1, maxi)
        print(hads)
        j = input()
    elif j == 'b' :
        mini = hads
        hads = random.randint(mini + 1, maxi)
        print(hads)
        j = input()
print("gg!")