def sumFunc(user): # 반복되는 부분을 함수화 시킨다.
    print(user+"야, 숫자 한 번 두 개 기깔나게 뽑아봐라.")
    num1 = int(input("정수1 ==>"))
    num2 = int(input("정수2 ==>"))
    hap = num1 + num2
    print("결과 : ", hap)

sumFunc("A")
sumFunc("B")
sumFunc("C")

''' # 결과 값을 따로 밖으로 빼내고 싶을 때 사용하는 코드.
def sumFunc(user): # 반복되는 부분을 함수화 시킨다.
    print(user+"야, 숫자 한 번 두 개 기깔나게 뽑아봐라.")
    num1 = int(input("정수1 ==>"))
    num2 = int(input("정수2 ==>"))
    hap = num1 + num2
    return hap # 값을 밖으로 출력할 때 사용함

hap = sumFunc("A")
print("결과", hap)

hap = sumFunc("B")
print("결과", hap)

hap = sumFunc("C")
print("결과", hap)
'''