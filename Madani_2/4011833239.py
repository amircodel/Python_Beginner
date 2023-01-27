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
        print('The normal form of a equation is ax**2+bx+c')
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
            print('answer are', x1 , 'and', x2)
        elif delta == 0 :
            x1 = -b / (2 * a)
            print('answer is', x1)
        elif delta < 0 :
            x1 = 'there is not any answer for this'
            print(x1)
        a = b = c = None
    elif choose == 2 :
        a = int(input('enter a six digits number:'))
        adigit = (a / 100000)
        if adigit >= 1 and adigit < 10 :
            a1 = a % 10
            a2 = int(a / 10) % 10
            a3 = int(a / 100) % 10
            a4 = int(a / 1000) % 10
            a5 = int(a / 10000) % 10
            a6 = int(a / 100000) % 10
            adigit2 = a1 + a2 + a3 + a4 + a5 + a6
            a10 = (adigit2 % 10) + (int(adigit2 / 10) % 10)
            a100 = (a10 % 10) + (int(a10 / 10) % 10)
            if (adigit2 / 10) < 1 :
                print()
                print(adigit2)
            elif (a10 / 10) <= 1 :
                print()
                print(a10)
            elif (a100 / 10) <= 1 :
                print()
                print(a100)
        else:
            print()
            print('please enter a six digits number!')
        a = adigit = adigit2 = a1 = a2 = a3 = a4 = a5 = a6 = a10 = a100 = None
    elif choose == 3 :
        print()
        a = int(input('enter a number:'))
        b = 1
        c = 0
        while b <= a :
            c += (b ** 2)
            b += 1
        print(c)
        a = b = c = None
    elif choose == 4 :
        print()
        a = int(input('enter a number:'))
        b = 1
        c = 0
        for i in range(b, a+1) :
            c += (b ** 2)
            b += 1
        print(c)
        a = b = c = None
    elif choose == 5 :
        print()
        import math
        a = int(abs(int(input('enter a number:'))))
        b = str(a) [::-1]
        print(b)
        a = b = None