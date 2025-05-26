def sumFunc(user): # 반복되는 부분을 함수화 시킨다.
    print(user+"야, 숫자 한 번 두 개 기깔나게 뽑아봐라.")
    num1 = int(input("정수1 ==>"))
    num2 = int(input("정수2 ==>"))
    hap = num1 + num2
    return hap # 값을 밖으로 출력할 때 사용함

def calc(v1, v2, op):
    value = 0

    if op == '+':
        value = v1+v2

    elif op == '-':
        value = v1-v2

    elif op == '*':
        value = v1*v2

    elif op == '/':
        value = v1/v2

    return value

op = input("계산 입력 (+, -, *, /")
v1 = int(input("첫번 째 숫자 입력 :"))
v2 = int(input("두번 째 숫자 입력 :"))
value = calc(v1, v2, op)
print("계산기 :", v1, op, v2, "=", value)