print ('세개의 정수 중에서 가장 적은 수를 찾아드리겠습니다.\n')

a = int(input('첫 번째 수: '))
b = int(input('두 번째 수: '))
c = int(input('세 번째 수: '))

if a < b and a < c:
    print('가장 적은수는', a , '입니다.')
elif b < a and b < c:
    print('가장 적은수는', b , '입니다.')
else:
    print('가장 적은수는', c , '입니다.')