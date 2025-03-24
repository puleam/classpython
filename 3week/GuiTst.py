import tkinter #Tkinter 는 root 라는 구조를 사용한다.
import tkinter.font

root = tkinter.Tk() #Tkinter 라이브러리를 담는 변수이자, 이를 담당함 / 윈도우 객체 생성
root.title("첫번 째 윈도우")

root.geometry("800x600") #사이즈

labelA = tkinter.Label(root, text="동", font=("한컴 말랑말랑 Regular", 24)) #만들고 나서 붙이는 것이 개념이다. root 에 속하기 때문에 root 를 맨 앞에 작성해준다.
labelB = tkinter.Label(root, text="서", font=("한컴 말랑말랑 Regular", 24)) #만들고 나서 붙이는 것이 개념이다. root 에 속하기 때문에 root 를 맨 앞에 작성해준다.
labelC= tkinter.Label(root, text="남", font=("한컴 말랑말랑 Regular", 24)) #만들고 나서 붙이는 것이 개념이다. root 에 속하기 때문에 root 를 맨 앞에 작성해준다.
labelD = tkinter.Label(root, text="북", font=("한컴 말랑말랑 Regular", 24)) #만들고 나서 붙이는 것이 개념이다. root 에 속하기 때문에 root 를 맨 앞에 작성해준다.

print(tkinter.font.families()) #font 값 출력

labelA.place(x=550, y=250) #윈도우에 라벨 배치
labelB.place(x=250, y=250) #윈도우에 라벨 배치
labelC.place(x=400, y=400) #윈도우에 라벨 배치
labelD.place(x=400, y=100) #윈도우에 라벨 배치

btn = tkinter.Button(root, text="버튼", font=("돋움", 24))
btn.place(x=400, y=250, height=32, width= 32)

root.mainloop() #화면이 꺼지지 않게 유지. 마지막에 넣는다.
