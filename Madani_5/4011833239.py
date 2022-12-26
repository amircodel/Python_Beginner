while True :
    list = ['1) Minimum string' , '2) Little numbers counter','3) Day of year' , '4) Pricing water', '5) Armstrong', '6) Dozz Dozz' , '7) Pro Dozz Dozz']
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
        pass
    elif choose == 7 :
        pass