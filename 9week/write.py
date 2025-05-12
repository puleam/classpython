outfile = open("C:/Users/user/Desktop/classpython/9week/outTest.txt","w",encoding="UTF-8")

while True :
    outStr = input("내용입력 ==>")
    # '끝' 이라고 입력하면 종료
    if outStr == '끝':
        break1
    outfile.writelines(outStr+"\n")

outfile.close()