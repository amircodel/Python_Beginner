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