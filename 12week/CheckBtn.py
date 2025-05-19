import tkinter
import random
import tkinter.messagebox

root = tkinter.Tk()
root.title('캔버스 만들기')

def mouseMove(event):
    x = event.x
    y = event.y
    labelMouse["text"]=str(x)+","+str(y)

root.bind("<Motion>", mouseMove)
labelMouse = tkinter.Label(root, text= ",", font=("맑은 고딕",10))
labelMouse.pack()

#체크버튼 클릭 시
def chkBtnClick():
    numCheck = 0
    if cvalue1.get() == True: numCheck += 1
    if cvalue2.get() == True: numCheck += 1
    if cvalue3.get() == True: numCheck += 1
    if cvalue4.get() == True: numCheck += 1
    if cvalue5.get() == True: numCheck += 1
    if cvalue6.get() == True: numCheck += 1
    if cvalue7.get() == True: numCheck += 1
    print(numCheck)
    textFiled.delete("1.0", tkinter.END)
    textFiled.insert("1.0","<진단결과>\n 당신의 고양이 지수는"
                     +str(int(numCheck/7*100))+"%입니다. \n"
                     +result[numCheck])

    def Btnclick():

    numCheck = 0
    if cvalue1.get() == True: numCheck += 1
    if cvalue2.get() == True: numCheck += 1
    if cvalue3.get() == True: numCheck += 1
    if cvalue4.get() == True: numCheck += 1
    if cvalue5.get() == True: numCheck += 1
    if cvalue6.get() == True: numCheck += 1
    if cvalue7.get() == True: numCheck += 1
    print(numCheck)


    result  = [
        '전생에 고양이었을 가능성은 매우 낮습니다.',
        '보통 사람입니다.',
        '특별히 이상한 곳은 없습니다.',
        '꽤 고양이다운 구석이 있습니다.',
        '고양이와 비슷한 성격 같습니다.',
        '고양이와 근접한 성격입니다.',
        '전생에 고양이었을지도 모릅니다.',
        '겉모습은 사람이지만, 속은 고양이일 가능성이 있습니다.'
    ]

'''

def chkBtnClick():
    if cvalue.get() == True:
        print("체크 되었습니다.")
        tkinter.messagebox.showinfo("제목","내용") #메세지 박스
        tkinter.messagebox.showwarning("제목","내용") #메세지 박스
        tkinter.messagebox.showerror("제목","내용") #메세지 박스
        answer = tkinter.messagebox.askyesno("제목","오징어 게임에 참가 하시겠습니까?") #메세지 박스
        if answer == True:
            print("동의")
        else:
            print("거절")
    else:
        print("체크가 해제 되었습니다.")


'''

        
root.geometry("800x600")

canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()

bgimg = tkinter.PhotoImage(file="C:/Users/user/Desktop/classpython/12week/img/mina.png")
canvas.create_image(400, 300, image=bgimg)

cvalue1 = tkinter.BooleanVar() #값을 저장하는 요소
cvalue2 = tkinter.BooleanVar() #값을 저장하는 요소
cvalue3 = tkinter.BooleanVar() #값을 저장하는 요소
cvalue4 = tkinter.BooleanVar() #값을 저장하는 요소
cvalue5 = tkinter.BooleanVar() #값을 저장하는 요소
cvalue6 = tkinter.BooleanVar() #값을 저장하는 요소
cvalue7 = tkinter.BooleanVar() #값을 저장하는 요소

cvalue1.set(False) #변수를 참으로 설정
cvalue2.set(False) #변수를 참으로 설정
cvalue3.set(False) #변수를 참으로 설정
cvalue4.set(False) #변수를 참으로 설정
cvalue5.set(False) #변수를 참으로 설정
cvalue6.set(False) #변수를 참으로 설정
cvalue7.set(False) #변수를 참으로 설정

cbtn1 = tkinter.Checkbutton(text="높은 곳이 좋다.", variable=cvalue1, command=chkBtnClick) #variable 로 cvalue 함수와 엮어준다.
cbtn2 = tkinter.Checkbutton(text="공을 보면 굴리고 싶어진다.", variable=cvalue2, command=chkBtnClick) #variable 로 cvalue 함수와 엮어준다.
cbtn3 = tkinter.Checkbutton(text="깜짝 놀라면 털이 곤두선다.", variable=cvalue3, command=chkBtnClick) #variable 로 cvalue 함수와 엮어준다.
cbtn4 = tkinter.Checkbutton(text="쥐구멍이 마음에 든다.", variable=cvalue4, command=chkBtnClick) #variable 로 cvalue 함수와 엮어준다.
cbtn5 = tkinter.Checkbutton(text="개에게 적대감을 느낀다.", variable=cvalue5, command=chkBtnClick) #variable 로 cvalue 함수와 엮어준다.
cbtn6 = tkinter.Checkbutton(text="생선 뼈를 발라 먹고 싶다.", variable=cvalue6, command=chkBtnClick) #variable 로 cvalue 함수와 엮어준다.
cbtn7 = tkinter.Checkbutton(text="밤, 기운이 난다.", variable=cvalue7, command=chkBtnClick) #variable 로 cvalue 함수와 엮어준다.

ygap = 40

cbtn1.place(x=402, y=185+ygap*0)
cbtn2.place(x=402, y=185+ygap*1)
cbtn3.place(x=402, y=185+ygap*2)
cbtn4.place(x=402, y=185+ygap*3)
cbtn5.place(x=402, y=185+ygap*4)
cbtn6.place(x=402, y=185+ygap*5)
cbtn7.place(x=402, y=185+ygap*6)

#곱하기 변수를 사용했을 때, 나중에 값을 하나하나 다 바꾸지 않아도 하나만 바꿀 수 있어서 편하다.

textFiled = tkinter.Text()
textFiled.place(x=330, y=50, width=420, height=90)

btn = tkinter.Button(text="진단하기",font=("맑은고딕",24),bg="#CFF7EB", command=BtnClick)
btn.place(x=430, y=480, width=150, height=60)


root.mainloop()