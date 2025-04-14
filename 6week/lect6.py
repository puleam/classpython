# for i in range(5,16,4): #첫값, 끝값, 증가값
#     print(i, '파이썬조아')


#팩토리아 계산기 1부터 N까지의 곱
# N = 5
# res = 1

# for i in range(N):
#     res = res * i
# print(res)


# for i in range(50,101,3):
#     print(i, end=" ") #줄바꿈 아니고, 일렬로 띄워쓰기 됨


# 연습1
# 1000 - 2000 사이에서 홀수의 합을 구하는 프로그램

# res = 0
# hap= 0

# for i in range(1001,2001,2):
#     hap += i
#     print("1000에서 2000 사이에서의 홀수의 합:",hap)


# # 500에서 1000 사이의 짝수 합
# i, hap = 0, 0

# for i in range(500, 1001, 2):
#     hap += i
#     print("1000에서 2000사이의 짝수 합: ", hap)

# for i in range(0,3,1):
#     for k in range(0,2,1):
#         #print("i : ",i,'    k:',k)
#         pass

# # 실습2
# # 당 신 이 개 처 몰 랐 던 사 실
# # 2단 ~ 9단 구구단
# for num1 in range(2,10,1): #단
#     print("----",num1,"단 ----")
#     for num2 in range(1,10,1): #곱해지는 수
#         print(num1,'x',num2,'=\t',num1*num2)
#     print("")

# i = 0
# while(i < 3):
#     print('ㅎ',end = "")
#     i = i + 1

#while문
# while(True):
#     num1 = int(input("숫자1 ==>"))
#     #num1 이 0 이면 반복문 종료
#     if num1 == 0:
#         break
#     num2 = int(input("숫자2 ==>"))
#     res = num1 + num2
#     print(num1,'+',num2,'=',res)

# 연습2
# 1부터 100까지를 더하되 4의 배수는 더하지 않음
# 3의 배수도 더하지 않음
res = 0
for i in range(1,101,1):
    if i%4 == 0: #i 가 4의 배수일 때,
        continue
    res = res + i
    print(res)