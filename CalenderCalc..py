Year = int(input("몇 년? "))
Month = int(input("몇 달? "))
Day = (Month*30)+(Year*365)

print(Year,'년', Month ,'개월은 날짜로 환산하면', Day , '일입니다.')