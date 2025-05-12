# test2.txt 파일을 읽어와서
# outTest.txt 파일에 작성한다.

Infile = open("C:/Users/user/Desktop/classpython/9week/test2.txt","r", encoding="UTF-8") #읽기 목적으로 해당 파일을 연다. 한글로 인코딩하기 위해 UTF-8
Outfile = open("C:/Users/user/Desktop/classpython/9week/outTest.txt","w",encoding="UTF-8")

while True:

    strFile = Infile.readline() #읽다
    if(str == ""):
        break

Outfile.writelines(strFile) #읽어 온 파일을 Outfile 에 넣는다.

Infile.close()
Outfile.close()