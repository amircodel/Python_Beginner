for i in range(50):
  print()
  print('1: first letter printer')
  print()
  print('2: Inch to CM')
  print()
  print('3: Rock paper scissors game')
  print()
  print('4: divisibility Finder')
  for i in range(3):
    print()
  choose = int(input('Choose once:'))
  if choose == 1 :
    #1
    name = input('enter your nicname:')
    cap = name[0]
    if cap == 'a' :
      for i in range(5):
        print()
      print('  **  ')
      print()
      print(' *  * ')
      print()
      print('*    *')
      print()
      print('******')
      print()
      print('*    *')
      print()
      print('*    *')
      print()
      print('*    *')
      print()
      print('*    *')
      for i in range(5):
        print()
      name = None
    else:
      print('sorry, I have not any plan for this :(')
      for i in range(3):
        print()
      print('  **  ')
      print()
      print(' **** ')
      for i in range(3):
        print()
      name = None
    choose = None
  elif choose == 2 :
    #2
    inch = input('enter your value by the Inch:')
    print(float(inch) * 2.54 ,"cm")
    inch = None
    choose = None
  elif choose == 3 :
    #3
    for i in range(5):
      print()
    print('1: Rock')
    print()
    print('2: Paper')
    print()
    print('3: Scissors')
    for i in range(3):
      print()
    choose2 = int(input('choose once:'))
    import random
    choose3 = random.randrange(1 , 4)
    if choose2 == choose3 :
      for i in range(3):
        print()
      print('draw')
    elif choose2 == 1 and choose3 == 2 :
      for i in range(3):
        print()
      print('You lose!')
    elif choose2 == 1 and choose3 == 3 :
      for i in range(3):
        print()
      print('You won!')
    elif choose2 == 2 and choose3 == 1 :
      for i in range(3):
        print()
      print('You won!')
    elif choose2 == 2 and choose3 == 3 :
      for i in range(3):
        print()
      print('You lose!')
    elif choose2 == 3 and choose3 == 1 :
      for i in range(3):
        print()
      print('You lose!')
    elif choose2 == 3 and choose3 == 2 :
      for i in range(3):
        print()
      print('You won!')
    choose2 = choose3 = None
    choose = None
  elif choose == 4 :
    #4
    num1 = int(input('enter first number:'))
    num2 = int(input('enter second number:'))
    if num1 % num2 == 0 or num2 % num1 == 0 :
      print('multiple')
    else:
      print('not')
