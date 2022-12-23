for i in range(100) :
    list = ['1) Risheh_sahih' , '2) eglidis_algorithm']
    for j in list :
        print()
        print(j)
    print()
    choose = int(input('Choose once:'))
    print()
    if choose == 1 :
        num1 = int(input('Enter a Number:'))
        numlist = [i for i in range(num1) if i ** 2 <= num1]
        print(max(numlist))
    elif choose == 2 :
        num2 = int(input('Enter a Number:'))    
        num3 = int(input('Enter a Number:'))
        numlist2 = [num2, num3]
        for i in range(100) :
            r1 = max(numlist2) / min(numlist2)
            r2 = max(numlist2) % min(numlist2)
            numlist2 = [min(numlist2), r2]
            if r2 == 0 :
                print(numlist2[0])
                break
    continue        