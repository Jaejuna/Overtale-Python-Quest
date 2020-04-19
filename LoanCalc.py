print('한양은행 대출 상환금 계산 서비스에 온신걸 환영합니다.')
Principal = int(input('대출 원근이 얼마인가요? (백만원 이상만) '))
Year = int(input('상환기간은 몇 년인가요?(년 단위로) ' ))
Interest = float(input('연 이자율은 몇% 인가요? (0.0에서 9.9 사이 수만) '))
Month = Year * 12
MonthInt = Interest /120
MonthlyPay  = (1 + MonthInt) ** Month * Principal * MonthInt / (1+MonthInt) ** Month - 1
Total = MonthlyPay * Year * 12

print('\n대출 상환금 내역을 알려드리겠습니다.\n'
      '대출 원금:', Principal , '원\n'
      '연 이자율 ', Interest , '%로', Year , '년 동안 매월 원리금 균등으로 상환하면\n'
      '매월 ', int(MonthlyPay) ,'원 씩 지불하셔야 합니다.\n'
      '상환 완료시 총 상환 금액은 ', int(Total) ,' 원 입니다.')