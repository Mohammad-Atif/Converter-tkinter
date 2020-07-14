from tkinter import *

def celtofar(c):
    f=(c*9/5)+32
    far=f"{f}"
    return far
def fartcel(f):
    c=(f-32)*5
    c=c/9
    cel=f"{c}"
    return  cel

px=80
py=10

window=Tk()
window.title("CONVERTER")
window.geometry('500x300')
window.resizable(0,0)

frame_into=Frame(window,height=100)
frame_into.pack(fill=X)
fram2=Frame(window,height=40)
fram2.pack(fill=X)
frame_conversion=Frame(window)
frame_conversion.pack(fill=BOTH)
frameconbtn=Frame(window,height=100)
frameconbtn.pack(fill=X)
intro_label=Label(frame_into,text="CONVERTER",font=("Arial Bold",50),fg="coral3",bg="LightBlue3")
intro_label.pack()
# intro_label.grid(row=0,column=0,padx=35)
var=IntVar()

def con_clicked(event):
    v=var.get()
    value=int(from_entry.get())
    res=0
    if(v==1):
        res=celtofar(value)
    if(v==2):
        res=fartcel(value)
    r=str(res)
    converted_label.configure(text=r)
def celtofarfun(event):
    from_label.configure(text="celcius")
    to_label.configure(text="farhenhiet")
def fartocelfun(event):
    from_label.configure(text="farhenhiet")
    to_label.configure(text="celcius")

celtofarbtn=Radiobutton(fram2,text="Cel to Far",variable=var,value=1)
fartocelbtn=Radiobutton(fram2,text="Far to Cel",variable=var,value=2)
fartocelbtn.bind("<Button-1>",fartocelfun)
celtofarbtn.bind("<Button-1>",celtofarfun)
celtofarbtn.grid(row=1,column=0,padx=px,pady=py)
fartocelbtn.grid(row=1,column=1,padx=px,pady=py)
from_label=Label(frame_conversion,text="from",font=("Arial",20))
from_label.grid(row=0,column=0,padx=py,pady=py)
to_label=Label(frame_conversion,text="to",font=("Arial",20))
to_label.grid(row=1,column=0,padx=px,pady=py)
from_entry=Entry(frame_conversion)
from_entry.grid(row=0,column=1,padx=0,pady=py)
converted_label=Label(frame_conversion,text="-----",bg="White")
converted_label.grid(row=1,column=1,padx=0,pady=py)
convert_btn=Button(frameconbtn,text="CONVERT",font=("Arial Bold",10))
convert_btn.bind("<Button-1>",con_clicked)
convert_btn.pack()

window.mainloop()