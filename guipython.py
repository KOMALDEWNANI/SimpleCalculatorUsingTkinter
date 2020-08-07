from tkinter import *
root=Tk()
root.title("Calculator")
root.geometry('350x460')
lbl1=Label(root,text="Hey there i am your calculator")
lbl1.grid(column=0,row=0)
lbl2=Label(root,text="Enter First Number")
lbl2.grid(column=0,row=1)
txt1=Entry(root,width=6)
txt1.grid(column=1,row=1)
lbl3=Label(root,text="Enter Second number")
lbl3.grid(column=0,row=2)
txt2=Entry(root,width=6)
txt2.grid(column=1,row=2)
lbl4=Label(root,text="")
lbl4.grid(column=1,row=4)

def Add():
    s=int(txt1.get())+int(txt2.get())
    lbl4.configure(text=s)

def Sub():
    s = int(txt1.get()) - int(txt2.get())
    lbl4.configure(text=s)
def Mult():
    s=int(txt1.get())*int(txt2.get())
    lbl4.configure(text=s)
def Div():
    s=int(txt1.get())/int(txt2.get())
    lbl4.configure(text=s)
b1=Button(root,text="Add",command=Add)
b1.grid(column=0,row=3)
b2=Button(root,text="Subtract",command=Sub)
b2.grid(column=1,row=3)
b3=Button(root,text="Multiply",command=Mult)
b3.grid(column=2,row=3)
b4=Button(root,text="Divide",command=Div)
b4.grid(column=3,row=3)



root.mainloop()








