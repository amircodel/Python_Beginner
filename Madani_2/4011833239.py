for i in range(50):
    print()
    print('1: 2nd degree equation')
    print()
    print('2: Sum of Digits')
    print()
    print('3: Sum of squares of consecutive numbers')
    print()
    print('4: Sum of squares of consecutive numbers by for')
    print()
    print('5: Reverse Digits')
    print()
    choose = int(input('choose once:'))
    if choose == 1 :
        print()
        a = int(input('enter a:'))
        print()
        b = int(input('enter b:'))
        print()
        c = int(input('enter c:'))
        delta = b**2 - 4 * a * c
        if delta > 0 :
            x1 = (-b + delta ** 0.5) / (2 * a)
            x2 = (-b - delta ** 0.5) / (2 * a)
            print('answer is', x1 , 'and', x2)
        elif delta == 0 :
            x1 = -b / (2 * a)
            print('answer is', x1)
        elif delta < 0 :
            x1 = 'there is not any answer for this'
            print(x1)