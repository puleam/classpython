import tkinter

## 전역 변수

tmr = 0

## 함수 선언
def countUp():
    global tmr
    tmr = tmr + 1 # 값이 점점 증가하는 변수
    label["text"] = tmr
    root.after(1000, countUp) # 특정한 함수를 실행 (스스로를 부르는 함수)

## 메인 함수
root = tkinter.Tk()
root.title("타이머")
root.geometry("300x200")
label = tkinter.Label(text=tmr, font=("궁서체",80))
label.pack()
root.after(1000, countUp) # 특정한 함수를 실행
root.mainloop()
