print ('\n 0 이상의 정수를 입력해주시면 윤년인지 평년인지 확인해드립니다. True는 윤년 False는 평년입니다.\n')

a = int(input('년도를 입력해 주세요: '))

if not a % 100 == 0 and a % 4 == 0 or a % 400 == 0:
    print(True)
else:
    print(False)
