import tkinter #Tkinter 는 root 라는 구조를 사용한다.
def click_btn(): #정의함수
    pass #버튼 누르면 동서남북이 나온다


    labelA = tkinter.Label(root, text="동", font=("한컴 말랑말랑 Regular", 24))
    labelB = tkinter.Label(root, text="서", font=("한컴 말랑말랑 Regular", 24))
    labelC= tkinter.Label(root, text="남", font=("한컴 말랑말랑 Regular", 24))
    labelD = tkinter.Label(root, text="북", font=("한컴 말랑말랑 Regular", 24))
    labelA.place(x=550, y=250) #윈도우에 라벨 배치
    labelB.place(x=250, y=250) #윈도우에 라벨 배치
    labelC.place(x=400, y=400) #윈도우에 라벨 배치
    labelD.place(x=400, y=100) #윈도우에 라벨 배치

    txt = entry.get()
    str1 = txt
    labeltxt = tkinter.Label(root, text=str1, font=("한컴 말랑말랑 Regular", 24)) #생성한 후에는 place로 위치 잡아주기
    labeltxt.place(x= 200, y= 300)


root = tkinter.Tk() #Tkinter 라이브러리를 담는 변수이자, 이를 담당함 / 윈도우 객체 생성
root.title("첫번 째 윈도우")

root.geometry("800x600") #사이즈

btn = tkinter.Button(root, text="버튼", font=("돋움", 8), command=click_btn)
btn.place(x=400, y=250, height=32, width= 32)

entry = tkinter.Entry(width=5)
entry.place(x=200, y=350)

root.mainloop() #화면이 꺼지지 않게 유지. 마지막에 넣는다.
