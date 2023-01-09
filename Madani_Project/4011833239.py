#!/usr/bin/env python
# -*- coding: utf-8 -*-
# امیرعلی محمدی
# 4011833239
n = input(':مبلغ را به تومان وارد کنید')
n = int(n)
if n > 10**60 :
    raise ValueError('the number you have entered is over than 10**60 .')
# تبدیل تومان به ريال
n *= 10
# دیکشنری فارسی عداد
dic1 = {0:'',1:'یک',2:'دو',3:'سه', 4:'چهار',5:'پنج',6:'شش',7:'هفت',8:'هشت',9:'نه', 10:'ده',11:'یازده',12:'دوازده',13:'سیزده',14:'چهارده',15:'پانزده',16:'شانزده',17:'هفده',18:'هجده',19:'نوزده',20:'بیست',30:'سی',40:'چهل',50:'پنجاه',60:'شصت',70:'هفتاد',80:'هشتاد',90:'نود',100:'صد',200:'دویست',300:'سیصد',400:'چهارصد',500:'پانصد',600:'ششصد',700:'هفتصد',800:'هشتصد',900:'نهصد'}
dic2 = {10**3:'هزار',10**6:'میلیون',10**9:'بیلیون',10**12:'تریلیون',10**15:'کوآدریلیون',10**18:'کوینتیلیون',10**21:'سکستیلیون',10**24:'سپتیلیون',10**27:'اکتیلیون',10**30:'نانیلیون',10**33:'دسیلیون',10**36:'آندسیلیون',10**39:'دیودسیلیون',10**42:'تریدسیلیون',10**45:'کواتیوردسیلیون',10**48:'کویندسیلیون',10**51:'سکسدسیلیون',10**54:'سپتدسیلیون',10**57:'اُکتودسیلیون',10**60:'نومدسیلیون'}
splitor = 'و '
q = ''
# ساختن تابع عملیات پروژه
def fun(l):
    global q
    def div(w): 
        lst1 = [i for i in w]
        lst2 = []
        va = len(w) - 1
        for i in range(va,-1,-1):
            for l in lst1:
                l = int(l)
                lst2.append(l*10**i)
                lst1.remove(str(l))
                break
        if sum(lst2[1:]) < 20 :
            mood = sum(lst2[1:])
            for i in lst2[1:] :
                lst2.remove(i)
            lst2.append(mood)
        return lst2
    l = str(l)
    list = [i for i in l]
    for i in range(len(l)-1,-1,-3) :
        if i == len(l)-1 :
            continue
        else:
            list[i] = list[i] + ','
            l = ''.join(list)
    list.clear()
    list = l.split(',')
    z = (len(list) - 1) * 3
    for r in list :
        if r != list[0] :
            z = ((z / 3) - 1)*3
        if int(r) > 20 :
            lst = div(r)
        else:
            lst = []
            lst.append(r)
        for c in lst:
            q += dic1.get(int(c))
            q += ' '
            if c != lst[len(lst)-1]:
                q += splitor
        q += dic2.get(10**z,"")
        q += ' '
        if r != list[len(list)-1]:
            q += splitor
    q = q.strip(splitor)
    return q
javab = fun(n) + ' ' + 'ريال'
print(javab)