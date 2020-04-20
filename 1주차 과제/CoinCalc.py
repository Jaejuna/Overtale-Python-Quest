print ('동전 합산 해드리겠습니다... 음수는 넣지마세요.\n' )

OhBack = int(input('오백원짜리 몇개? '))
Back = int(input('백원짜리 몇개? '))
OhShip = int(input('오십원짜리 몇개? '))
Ship = int(input('십원짜리 몇개? '))
Total = (OhBack*500) + (Back*100) + (OhShip * 50) + (Ship *10)

print ('\n 당신이 갖고 있는 동전은 총', Total, '원 입니다.' )