x = input().lower().replace('a','').replace('e', '').replace('i', '').replace('o','').replace('u', '')
letter = ''
for l in x:
    s = "." + l
    letter += s
print(letter)