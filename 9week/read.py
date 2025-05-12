import tkinter

root = tkinter.Tk()


file = open("C:/Users/user/Desktop/classpython/9week/test2.txt","r", encoding="UTF-8") #읽기 목적으로 해당 파일을 연다. 한글로 인코딩하기 위해 UTF-8

strFile = file.readline()
root.geometry(strFile[:-1])

strFile = file.readline()
root.title(strFile[:-1])

file.close()



# for i in range(0, 20, 1):

#     str = file.readline() #읽다
#     print(str, end="")

# str = file.readline() #파일이 끝나면 str은 비워지게 된다. 그럴 경우 끝?을 출력
# if(str == ""):
#     print("끝?")

'''
fileList = file.readlines() #파일의 있는 모든 값을 이곳에 저장함
index = 1
for strList in fileList :
    print(str(index)+" : "+strList, end ="")    
    index = index + 1
file.close() #닫다

'''


'''
while True:

    str = file.readline() #읽다
    print(str, end="")
    if(str == ""):
        break
'''
