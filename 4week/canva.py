import tkinter
root = tkinter.Tk()

#캔버스 설정
root.title("첫번 째 캔버스") #root 와 캔버스는 상하관계로 엮인다. 연결 되어있음.
canvas = tkinter.Canvas(root, width=400, height=600) 
canvas.pack()

#캔버스 내 이미지 설정
bgimg = tkinter.PhotoImage(file="miko.png") #root, canvas bgimg는 일렬로 서로 연결 되어있다.
canvas.create_image(200, 300, image=bgimg) #객체화해서 생각하기. (어떤 거 안에 이게 있다. 쉬운 구조 이해)

root.mainloop()