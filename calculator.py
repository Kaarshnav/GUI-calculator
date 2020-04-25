from tkinter import *
from math import sin
root=Tk()
root.title('Calculator')
e=Entry(root,width=30,borderwidth=5)
e.grid(row=0,column=0,columnspan=4)
def equals():
    secno=e.get()
    e.delete(0,END)
    if math=='add':
        e.insert(0,int(secno)+int(fno))
    if math=='subs':
        e.insert(0,int(fno)-int(secno))
    if math=='div':
        e.insert(0,int(fno)/int(secno))
    if math=='mul':
        e.insert(0,int(secno)*int(fno))
    if math=='sinx':
        e.insert(0,sin(int(secno)))
    if math=='expo':
        e.insert(0,int(fno)**int(secno))

def sinx():
    global math
    math='sinx'
    e.delete(0,END)
def expo():
    curr=e.get()
    global fno
    global math
    math='expo'
    fno=curr
    e.delete(0,END)



def add():
    curr=e.get()
    global fno
    global math
    math='add'
    fno=curr
    e.delete(0,END)
def subs():
    curr=e.get()
    global fno
    global math
    math='subs'
    fno=curr
    e.delete(0,END)
def div():
    curr=e.get()
    global fno
    global math
    math='div'
    fno=curr
    e.delete(0,END)
def mul():
    curr=e.get()
    global fno
    global math
    math='mul'
    fno=curr
    e.delete(0,END)


def clear():
    e.delete(0,END)
def fn(num):
    currno=e.get()
    e.delete(0,END)
    newnum=str(currno)+str(num)
    e.insert(0,newnum)




butt1=Button(root,bg="pink",command=lambda :fn(1) ,width=5,borderwidth=5,text='1',padx=20,pady=10)
butt2=Button(root,bg="pink",command=lambda :fn(2),width=5,borderwidth=5,text='2',padx=20,pady=10)
butt3=Button(root,bg="pink",command=lambda :fn(3),width=5,borderwidth=5,text='3',padx=20,pady=10)
butt4=Button(root,bg="pink",command=lambda :fn(4),width=5,borderwidth=5,text='4',padx=20,pady=10)
butt5=Button(root,bg="pink",command=lambda :fn(5) ,width=5,borderwidth=5,text='5',padx=20,pady=10)
butt6=Button(root,bg="pink",command=lambda :fn(6) ,width=5,borderwidth=5,text='6',padx=20,pady=10)
butt7=Button(root,bg="pink",command=lambda :fn(7) ,width=5,borderwidth=5,text='7',padx=20,pady=10)
butt8=Button(root,bg="pink",command=lambda :fn(8) ,width=5,borderwidth=5,text='8',padx=20,pady=10)
butt9=Button(root,bg="pink",command=lambda :fn(9) ,width=5,borderwidth=5,text='9',padx=20,pady=10)
butt0=Button(root,bg="pink",command=lambda :fn(0) ,width=5,borderwidth=5,text='0',padx=20,pady=10)
buttclr=Button(root,bg="pink",command=clear ,width=17,borderwidth=5,text='Clear',padx=20,pady=10)
butteq=Button(root,bg="pink",command=equals ,width=17,borderwidth=5,text='=',padx=20,pady=10)

buttm=Button(root,bg="pink",command=mul ,width=5,borderwidth=5,text='*',padx=20,pady=10)
buttd=Button(root,bg="pink",command=div,width=5,borderwidth=5,text='/',padx=20,pady=10)
buttad=Button(root,bg="pink",command=add ,width=5,borderwidth=5,text='+',padx=20,pady=10)
buttsub=Button(root,bg="pink",command=subs ,width=5,borderwidth=5,text='-',padx=20,pady=10)
buttexp=Button(root,bg="pink",command=expo ,width=5,borderwidth=5,text='^',padx=20,pady=10)
buttsin=Button(root,bg="pink",command=sinx ,width=5,borderwidth=5,text='sin(x)',padx=20,pady=10)



butt7.grid(row=1,column=0)
butt8.grid(row=1,column=1)
butt9.grid(row=1,column=2)
butt4.grid(row=2,column=0)
butt5.grid(row=2,column=1)
butt6.grid(row=2,column=2)
butt3.grid(row=3,column=0)
butt2.grid(row=3,column=1)
butt1.grid(row=3,column=2)
butt0.grid(row=4,column=0)
buttclr.grid(row=4,column=1,columnspan=2)
butteq.grid(row=5,column=1,columnspan=2)

buttm.grid(row=1,column=3)
buttd.grid(row=2,column=3)
buttad.grid(row=3,column=3)
buttsin.grid(row=4,column=3)
buttexp.grid(row=5,column=3)
buttsub.grid(row=5,column=0)


mainloop()


