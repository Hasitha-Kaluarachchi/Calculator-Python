from tkinter import *

root=Tk()
root.title('smart calculator')
root.config(bg='deepskyblue2')
root.geometry('680x486+100+100')

entryField=Entry(root,font=('arial',20,'bold'),bg='deepskyblue2',fg='white',bd=10,relief=SUNKEN,width=30)
entryField.grid(row=0,column=0)

root.mainloop() 