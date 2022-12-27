while True :
    list = ['1) Minimum string' , '2) Little numbers counter','3) Day of year' , '4) Pricing water', '5) Armstrong', '6) Dozz Dozz']
    for i in list :
        print()
        print(i)
    print()
    choose = int(input('Choose once:'))
    print()
    if choose == 1 :
        def minimum(para) :
            print(min(para))
        s = input('enter a string:')
        minimum(s)
    elif choose == 2 :
        matrix = []
        for i in range(4) :
            row_list = []
            num = 0
            for i in range(4) :
                del num
                num = int(input('Enter a value:'))
                row_list.append(num)
            matrix.append(row_list)
        def matrixm(demo) :
            mig = []
            miig = []
            mim = []
            mim1 = []
            mim2 = []
            mim3 = []
            for i in range(4) :
                mig.append(demo[i][i])
            miig.append((demo[0][3]))
            miig.append((demo[1][2]))
            miig.append((demo[2][1]))
            miig.append((demo[3][0]))        
            mig = sum(mig) + sum(miig)
            for i in range(4) :
                mim.append(demo[0][i])
                mim1.append(demo[i][3])
                mim2.append(demo[3][i])
                mim3.append(demo[i][0])
            print(mim,mim1,mim2,mim3)
            mim = sum(mim) + sum(mim1) + sum(mim2) + sum(mim3)
            print(mim)
            if mig == mim :
                print('YES')
            else:
                print('NO')
        matrixm(matrix)
    elif choose == 3 :
        def rooz(day) :
            mahe31 = ['Farvardin', 'Ordibehesht', 'Khordad', 'Tir', 'Mordad', 'Shahrivar']
            mahe30 = ['Mehr', 'Aban', 'Azar', 'Day', 'Bahman']
            mahe29 = ['Esfand']
            if day >= 1 and day <= 31 :
                mahe = mahe31[0]
                rmahe = d
                print()
                print('%dth day of year, Bahar , %s , %dth day of the month.' %(d, mahe, rmahe))
            elif day > 31 and day <= 62 :
                mahe = mahe31[1]
                rmahe = d % 31
                print()
                print('%dth day of year, Bahar , %s , %dth day of the month.' %(d, mahe, rmahe))
            elif day > 62 and day <= 93 :
                mahe = mahe31[2]
                rmahe = d % 31
                print()
                print('%dth day of year, Bahar , %s , %dth day of the month.' %(d, mahe, rmahe))
            elif day > 93 and day <= 124 :
                mahe = mahe31[3]
                rmahe = d % 31
                print()
                print('%dth day of year, Tabestan , %s , %dth day of the month.' %(d, mahe, rmahe))
            elif day > 124 and day <= 156 :
                mahe = mahe31[4]
                rmahe = d % 31
                print()
                print('%dth day of year, Tabestan , %s , %dth day of the month.' %(d, mahe, rmahe))
            elif day > 156 and day <= 187 :
                mahe = mahe31[5]
                rmahe = d % 31
                print()
                print('%dth day of year, Tabestan , %s , %dth day of the month.' %(d, mahe, rmahe))
            elif day > 187 and day <= 217 :
                mahe = mahe30[0]
                rmahe = (d - 186) % 30
                print()
                print('%dth day of year, Paeiz , %s , %dth day of the month.' %(d, mahe, rmahe))
            elif day > 217 and day <= 247 :
                mahe = mahe30[1]
                rmahe = (d - 186) % 30
                print()
                print('%dth day of year, Paeiz , %s , %dth day of the month.' %(d, mahe, rmahe))
            elif day > 247 and day <= 277 :
                mahe = mahe30[2]
                rmahe = (d - 186) % 30
                print()
                print('%dth day of year, Paeiz , %s , %dth day of the month.' %(d, mahe, rmahe))
            elif day > 277 and day <= 307 :
                mahe = mahe30[3]
                rmahe = (d - 186) % 30
                print()
                print('%dth day of year, Zemestan , %s , %dth day of the month.' %(d, mahe, rmahe))
            elif day > 307 and day <= 337 :
                mahe = mahe30[4]
                rmahe = (d - 186) % 30
                print()
                print('%dth day of year, Zemestan , %s , %dth day of the month.' %(d, mahe, rmahe))
            elif day > 337 and day <= 365 :
                mahe = mahe29[0]
                rmahe = (d - 336) % 29
                print()
                print('%dth day of year, Zemestan , %s , %dth day of the month.' %(d, mahe, rmahe))
        d = int(input('enter a day num: '))
        rooz(d)
    elif choose == 4 :
        mas = int(input('enter used value (Per M**3): '))
        gem = input('enter type of usage (H/I/E): ')
        def mohasebe(megdar , type) :
            # fagad beh ezayeh 100 m**3 mohasebeh shoodeh
            if type == 'h' or gem == 'H' :
                megdar = (megdar // 100) * 500
                return megdar
            if type == 'i' or gem == 'I' :
                if megdar >= 4000000 :
                    megdar = (megdar // 1000) * 750
                    return megdar
                else:
                    megdar = ((megdar - 4000000)) * 0.00025 + (4000000 // 1000) * 750
                    return megdar
            if type == 'e' or gem == 'E' :
                if megdar >= 2000000 :
                    megdar = (megdar // 1500) * 600
                    return megdar
                else:
                    megdar = ((megdar - 2000000)) * 0.00004 + (2000000 // 1500) * 600
                    return megdar
        print(mohasebe(mas,gem), 'Ryal')
    elif choose == 5 :
        num = int(input('enter a number: '))
        def armstrong(n) :
            cou = len(str(n))
            numlist = []
            newlist = []
            for l in str(n) :
                numlist.append(int(l))
            for i in numlist :
                newlist.append((i ** cou))
            res = sum(newlist)
            if res == n :
                return 'Is Armstrong'
            else:
                return 'Is not Armstrong'
        print(armstrong(num))
    elif choose == 6 :
        matrix = []
        row= int(input("Enter number of rows:"))
        for i in range(row) :
            row_list = []
            num = 0
            for i in range(row) :
                del num
                num = '.'
                row_list.append(num)
            matrix.append(row_list)
        for i in matrix :
            print(i)
        choosen = []
        def pointchecker():
            pointlist = []
            for i in matrix :
                for j in i :
                    pointlist.append(j)
            return pointlist
        def winchecker():
            global keled
            from math import ceil
            matrix1 = []
            matrix3 = []
            matrix4 = []
            matrix5 = []
            matrix6 = []
            matrix7 = []
            matrix8 = []
            for i in range(row):
                matrix1.append(matrix[i][i])
                matrix3.append(matrix[0][i])
                matrix4.append(matrix[i][row - 1])
                matrix5.append(matrix[row - 1][i])
                matrix6.append(matrix[i][0])
                matrix7.append(matrix[(ceil(row/2) - 1)][i])
                matrix8.append(matrix[i][(ceil(row/2) - 1)])
            matrix2 = []
            for i in range(row -1 , -1 , -1) :
                matrix2.append(matrix[i][i])
            if matrix1 == ['U','U','U'] or matrix2 == ['U','U','U'] or matrix3 == ['U','U','U'] or matrix4 == ['U','U','U'] or matrix5 == ['U','U','U'] or matrix6 == ['U','U','U'] or matrix7 == ['U','U','U'] or matrix8 == ['U','U','U'] :
                print('YOU WON!')
                keled = 0
            elif matrix1 == ['C','C','C'] or matrix2 == ['C','C','C'] or matrix3 == ['C','C','C'] or matrix4 == ['C','C','C'] or matrix5 == ['C','C','C'] or matrix6 == ['C','C','C'] or matrix7 == ['C','C','C'] or matrix8 == ['C','C','C'] :
                print('YOU LOSE!')
                keled = 0
        keled = 1
        while '.' in pointchecker() and keled == 1 :
            import random
            # (row,col) ==> for example 2,4
            def x21():
                inp = input('Choose your cell (row,col): ')
                inp = inp.split(',')
                inpdic = dict()
                inpdic[int(inp[0])] = int(inp[1])
                if inpdic not in choosen :
                    choosen.append(inpdic)
                    for k,v in inpdic.items() :
                        matrix[k][v] = 'U'
                else:
                    x21()
            x21()
            def x22() :
                def genertion():
                    global inpdic2
                    inp2 = random.randint(0 , row - 1)
                    inp3 = random.randint(0 , row - 1)
                    inpdic2 = dict()
                    inpdic2[inp2] = inp3
                genertion()
                if inpdic2 not in choosen :
                    choosen.append(inpdic2)
                    for k,v in inpdic2.items() :
                        matrix[int(k)][int(v)] = 'C'
                    winchecker()
                else:
                    x22()
            x22()
            for i in matrix :
                print(i)