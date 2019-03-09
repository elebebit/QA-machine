import tkinter as tk
import os
import random
import json
#------------------创建问题集-----------------------------
dirfile='ques' #文件夹名字
qusfile=os.listdir(dirfile) #文件列表

quesl=[] #问题list
ansl=[] #答案list

qfl=random.sample(qusfile,4) #随机抽选不重复问题文件
print(qfl)

for i in range(len(qfl)):
	with open('ques/'+qfl[i]) as f:
		qs=json.load(f)
		for k,v in qs.items():
			quesl.append(k)
			ansl.append(v)

#------------------创建UI-----------------------------

window = tk.Tk()
window.title('Q&A')
window.geometry('500x541')

#-------------------bg--------------------------------

canvas = tk.Canvas(window, bg='white', height=500, width=541)
canvas.pack(side='left')
image_file = tk.PhotoImage(file='bg1.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)

#------------------function---------------------------

def Nextques():
	global n
	if n<=len(quesl)-1:
		var_title.set('Question '+str(n+1))
		var_n.set(quesl[n])
		n+=1
	else:
		var_title.set('')
		var_n.set('Over')

def Ans():
	global ans
	if ans==False:
		ans=True
		var_a.set(ansl[n-1])   
	else:
		ans=False
		var_a.set('')


#----------------------------------------------------		
var_title= tk.StringVar()
var_n = tk.StringVar()    # 这时文字变量储存器
var_a = tk.StringVar()    # 这时文字变量储存器
ans=False
n=0

lt = tk.Label(window, 
    textvariable=var_title,   # 使用 textvariable 替换 text, 因为这个可以变化
    bg='white',font=('Arial', 15), width=15, height=2)
lt.place(x=190,y=10,anchor='nw') 

#---------------------Next----------------------------

ln = tk.Label(window, 
    textvariable=var_n,   # 使用 textvariable 替换 text, 因为这个可以变化
    bg='white',font=('Arial', 15), width=40, height=5)
ln.place(x=90,y=100,anchor='nw') 

bn = tk.Button(window, 
    text='next', font=('Arial', 20),     # 显示在按钮上的文字
    width=8, height=3, 
    command=Nextques)     # 点击按钮式执行的命令
bn.place(x=190,y=200,anchor='nw')     # 按钮位置

#---------------------Ans-----------------------------

la = tk.Label(window, 
    textvariable=var_a,   # 使用 textvariable 替换 text, 因为这个可以变化
    bg='white', font=('Arial', 15), width=40, height=5)
la.place(x=90,y=300,anchor='nw')  
ba = tk.Button(window, 
    text='ans', font=('Arial', 20),     # 显示在按钮上的文字
    width=8, height=3, 
    command=Ans)     # 点击按钮式执行的命令
ba.place(x=190,y=400,anchor='nw')     # 按钮位置
#-------------------------------------------------


window.mainloop()