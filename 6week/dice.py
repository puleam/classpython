import random

dice1 = 0
dice2 = 0
dice3 = 0
count = 0

while(True):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    count = count + 1
    print(count, '회', dice1, dice2, dice3)

    #주사위 눈 확인(종료)
    if ((dice1 == dice2) and (dice2 == dice3)):
        break
    
    print('3개 주사위는 모두',dice1,'입니다.')
    print('같은 숫자가 나올 때 까지',count,'번 던졌습니다.')