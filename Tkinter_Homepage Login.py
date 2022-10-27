from tkinter import *
from tkinter import messagebox

window=Tk()
window.title('PT Mattel Indonesia')
window.geometry('925x500+300+200')
window.configure(bg="#fff")
window.resizable(False,False)

img = PhotoImage(file='mattel.png')
Label(window,image=img,bg='white').place(x=50,y=50)

frame=Frame(window,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='AUTOMATION Login', fg='#CC0000', bg='white', font=('Microsoft YaHei UI Light', 25, 'bold'))
heading.place(x=15,y=5)

user = Entry(frame,width=25, fg='black', border=2, bg="white", font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'User')
user = Entry(frame,width=25, fg='black', border=2, bg="white", font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=120)
user.insert(0,'Password')

window.mainloop()