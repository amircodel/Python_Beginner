while True:
    list = ['1) Array index switch' , '2) Little numbers counter','3) Symmetrical matrixs' , '4) Sparse matrix']
    for i in list :
        print()
        print(i)
    print()
    choose = int(input('Choose once:'))
    print()
    if choose == 1 :
        list2 = []
        choose2 = int(input('How many indexs you want to enter to your array:'))
        for _ in range(choose2) :
            index = int(input('enter the Number:'))
            list2.append(index)
        list4 = []
        for i in range(choose2) :
            list3 = []
            for j in list2[i+1:] :
                list3.append(j)
            list4.append(max(list3 , default=-1))
        print(list4)
        del list2 , list3 , list4 , choose2 , index
    elif choose == 2 :
        list2 = []
        choose2 = int(input('How many indexs you want to enter to your array? :'))
        for _ in range(choose2) :
            index = int(input('enter the Number:'))
            list2.append(index)
        list3 = []
        for i in range(choose2):
            x = 0
            for j in list2[i+1:]:
                if list2[i] > j :
                    x += 1
            list3.append(x)
        print(list3)
        del list2 , list3 , choose2 , index
    elif choose == 3 :
        matrix = []
        row= int(input("Enter number of rows:"))
        col= int(input("Enter number of column:"))
        for i in range(row) :
            row_list = []
            num = 0
            for i in range(col) :
                del num
                num = int(input('Enter a value:'))
                row_list.append(num)
            matrix.append(row_list)
        if row != col :
            print('The Matrix have you enterd is not a Symmetrical matrix')
        # create Symmetrical matrix
        else:
            d_matrix = []
            u_matrix= []
            for i in range(row - 1, 0, -1):
                for j in range(row - 2, -1, -1):
                    d_matrix.append(matrix[i][j])
                    u_matrix.append(matrix[j][i])
            if d_matrix == u_matrix :
                print('The Matrix have you enterd is a Symmetrical matrix!')
            else:
                print('The Matrix have you enterd is not a Symmetrical matrix')
        del u_matrix, d_matrix, num, row_list, col, row, matrix
    elif choose == 4:
        matrix = []
        row= int(input("Enter number of rows:"))
        col= int(input("Enter number of column:"))
        for i in range(row) :
            for i in range(col) :
                num = int(input('Enter a value:'))
                matrix.append(num)
        zero = 0
        for i in matrix:
            if i == 0 :
                zero += 1
        if (row * col)/2 <= zero :
            print('The Matrix have you enterd is a Sparse matrix!')
        else:
            print('The Matrix have you enterd is not a Sparse matrix')
        del row, col, zero, matrix, num