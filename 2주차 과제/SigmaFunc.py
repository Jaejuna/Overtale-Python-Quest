print('\nSigma Function을 원하면 1을 입력, Fatorial Function을 원하면 0을 입력해주세요\n')

a = int(input('원하는 함수를 선택해 주세요 (1 or 0): '))

while a != True and a != False:
    while True:
        r = int(input('1이나 0로 다시 입력해주세요: '))

        if  r == True:
            b = int(input("\nSigma Function 입니다. 함수에 넣을 숫자를 입력해주세요: "))
            Sig = 1
            while True:
                Sig = Sig + b
                b = b -1
                if b == 1:
                    break
            print('결과값은', Sig ,'입니다.')

        elif r == False:
            c = int(input('\nFactorial Function 입니다. 함수에 넣을 숫자를 입력해주세요: '))
            Fac = 1
            while True:
                Fac = Fac * c
                c = c-1
                if c == 0:
                    break
            print('결과값은', Fac ,'입니다.')