age = int(input())
if age > 0 and age < 6 :
    print('Minor')
elif age >= 6 and age < 10 :
    print('Kid')
elif age >= 10 and age < 14 :
    print('teenager')
elif age >= 14 and age < 24 :
    print('young')
elif age >= 24 and age < 40 :
    print('adult')
elif age >= 40 :
    print('Middle-aged')
