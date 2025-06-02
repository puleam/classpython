import tkinter

# 전역 변수
key = 0
cx  = 400
cy = 300    
# 함수 영역

# 키보드 입력으로 위치 변경
def mainProc():
 #   label['text']= key
    global cx, cy
    if key == 'Up':
        cy -= 20
    if key == 'Down':
        cy += 20
    if key == 'Left':
        cx = cx - 20
    if key == 'Right':
        cx = cx + 20

    # 변경된 위치의 경계를 확인
    if cy < 80 : cy = 80
    if cy > 600-100 : cy = 600-100
    if cx < 80 : cx = 80
    if cx > 800-100: cx = 800-100

    # 시간에 따라 캐릭터가 내려감
    cy += 10

    # 변경된 위치에 이미지를 옮김
    canvas.coords("chonsic",cx,cy)
    root.after(100, mainProc) # 자기 자신을 다시 호출

def key_down(e):
    global key #전역 변수 함수
    key = e.keysym #Keycode

def key_up(e):
    global key
    key = 0

# 메인 영역
root = tkinter.Tk()
root.title("키 이벤트")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
#label = tkinter.Label(font=("맑은 고딕", 80))
#label.pack()
canvas = tkinter.Canvas(width=800, height=600,bg='skyblue')
canvas.pack()

img = tkinter.PhotoImage(file="C:/Users/user/Desktop/classpython/14week/chonsic.png")
canvas.img = img
canvas.create_image(400,300, image=img, tag="chonsic")

mainProc()
root.mainloop() 