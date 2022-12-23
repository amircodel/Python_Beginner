x = input().lower()
def reverser(ch):
    return ch[::-1]
if x == reverser(x):
    print('palindrome')
else:
    print('not palindrome')