from tkinter import *
from tkinter.messagebox import *
from math import pi

def show_answer():
    Ans = (int(num1.get()))*(int(num2.get()))
    blank.insert(0, Ans)

def clear_rect():
    clear_rectangle = " "
    blank.insert(0, clear_rectangle)

def show_square():
    Sqr = ((int(side.get())))**2
    sqr_area.insert(0, Sqr)

def clear_square():
    sqr_area.delete(0, 'end')

def show_circle():
    Cir = ((int(radius.get()))**2)*(pi)
    circle_area.insert(0, Cir)
    
def clear_circle():
    circle_area.delete(0, 'end')

def show_rhombus():
    Rhom = ((int(diagonal1.get()))*(int(diagonal2.get())))/2
    rhombus_area.insert(0, Rhom)
    
def show_parallel():
    Para = (int(base.get()))*(int(height.get()))
    parallel_area.insert(0, Para)
    
def show_hemi():
    Hemi = ((int(radiushemi.get()))**2)*(pi)
    hemi_area.insert(0, Hemi)

    
main = Tk()
main.Title()
Label(main, text = "Rectangle").grid(row=0)
Label(main, text = "Enter Side 1:").grid(row=1)
Label(main, text = "Enter Side 2:").grid(row=2)
Label(main, text = "The Area is:").grid(row=3)

Label(main, text = "").grid(row=5)
Label(main, text = "Square").grid(row=7)
Label(main, text = "Enter Side").grid(row=8)
Label(main, text = "The Area is").grid(row=9)

Label(main, text = "").grid(row=11)
Label(main, text = "Circle").grid(row=12)
Label(main, text = "Enter Radius").grid(row=13)
Label(main, text = "The Area is").grid(row=14)

Label(main, text = "").grid(row=16)
Label(main, text = "Rhombus").grid(row=17)
Label(main, text = "Enter Diagonal 1:").grid(row=18)
Label(main, text = "Enter Diagonal 2:").grid(row=19)
Label(main, text = "The Area is:").grid(row=20)

Label(main, text = "").grid(row=22)
Label(main, text = "Parallelogram").grid(row=23)
Label(main, text = "Enter Base").grid(row=24)
Label(main, text = "Enter Height:").grid(row=25)
Label(main, text = "The Area is:").grid(row=26)

Label(main, text = "").grid(row=27)
Label(main, text = "Hemisphere").grid(row=0, column=9)
Label(main, text = "Enter radius").grid(row=1, column =9)
Label(main, text = "The Surface Area is").grid(row=2, column=9)


num1 = Entry(main)
num2 = Entry(main)
blank = Entry(main)
side = Entry(main)
sqr_area = Entry(main)
radius = Entry(main)
circle_area = Entry(main)
diagonal1=Entry(main)
diagonal2=Entry(main)
rhombus_area=Entry(main)
base=Entry(main)
height=Entry(main)
parallel_area=Entry(main)
radiushemi=Entry(main)
hemi_area=Entry(main)


num1.grid(row=1, column=1)
num2.grid(row=2, column=1)
blank.grid(row=3, column=1)
side.grid(row=8, column=1)
sqr_area.grid(row=9, column=1)
radius.grid(row=13, column=1)
circle_area.grid(row=14, column=1)
diagonal1.grid(row=18, column=1)
diagonal2.grid(row=19, column=1)
rhombus_area.grid(row=20, column=1)
base.grid(row=24, column=1)
height.grid(row=25, column=1)
parallel_area.grid(row=26, column=1)
radiushemi.grid(row=1, column=10)
hemi_area.grid(row=2, column=10)


Button(main, text='Quit', command=main.destroy).grid(row=4, column=0, sticky=W, pady=4)
Button(main, text='Show', command=show_answer).grid(row=4, column=1, sticky=W, pady=4)
Button(main, text="Clear", command=clear_rect).grid(row=4, column=2, sticky=W, pady=4)
Button(main, text="Show", command=show_square).grid(row=10, column=1, sticky=W, pady=4)
Button(main, text="Clear", command=clear_square).grid(row=10, column=2, sticky=W, pady=4)
Button(main, text="Show", command=show_circle).grid(row=15, column=1, sticky=W, pady=4)
Button(main, text="Clear", command=clear_circle).grid(row=15, column=2, sticky=W, pady=4)
Button(main, text="Show", command=show_rhombus).grid(row=21, column=2, sticky=W, pady=4)
Button(main, text="Show", command=show_parallel).grid(row=27, column=2, sticky=W, pady=4)
Button(main, text="Show", command=show_hemi).grid(row=3, column=11, sticky=W, pady=4)

mainloop()
