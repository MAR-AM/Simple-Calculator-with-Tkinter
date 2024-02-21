from tkinter import *
root = Tk()
root.title("calculator")
en = Entry(root, width=46, borderwidth=5,bg="#C1FFC1")
en.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def Button_click(number) :
    num = en.get()
    en.delete(0, END)
    en.insert(0, str(num) + str(number))


def Button_add() :
    global cal 
    cal = "add"
    global f_num
    f_num = int(en.get())
    en.delete(0, END)

def Button_mins():
    global cal
    cal = "mins"
    global f_num
    f_num = int(en.get())
    en.delete(0, END) 

def Button_mult():
    global cal
    cal = "mult"
    global f_num
    f_num = int(en.get())
    en.delete(0, END)

def Button_devide():
    global cal
    cal = "div"
    global f_num
    f_num = int(en.get())
    en.delete(0, END)


def clear():
    en.delete(0, END)

def button_Equal():
    if cal == "add" :
       second_num = en.get()
       en.delete(0, END)
       en.insert(0, f_num + int(second_num))
    if cal == "mins" :
       second_num = en.get()
       en.delete(0, END)
       en.insert(0, f_num - int(second_num))
    if cal == "mult" :
       second_num = en.get()
       en.delete(0, END)
       en.insert(0, f_num * int(second_num))
    try :
        if cal == "div" :
            second_num = en.get()
            en.delete(0, END)
            if second_num != 0 :
                en.insert(0, f_num / int(second_num))
    except ZeroDivisionError:
        en.insert(0,"ERROR")
    


my_button_1  = Button(root,bg="#BDFCC9",text="1", padx=40, pady=20, command=lambda: Button_click(1))
my_button_2  = Button(root,bg="#BDFCC9" ,text="2", padx=40, pady=20, command=lambda: Button_click(2))
my_button_3  = Button(root,bg="#BDFCC9", text="3", padx=40, pady=20, command=lambda: Button_click(3))
my_button_4  = Button(root,bg="#EEEE00", text="4", padx=40, pady=20, command=lambda: Button_click(4))
my_button_5  = Button(root,bg="#EEEE00", text="5", padx=40, pady=20, command=lambda: Button_click(5))
my_button_6  = Button(root,bg="#EEEE00", text="6", padx=40, pady=20, command=lambda: Button_click(6))
my_button_7  = Button(root,bg="#FFB6C1", text="7", padx=40, pady=20, command=lambda: Button_click(7))
my_button_8  = Button(root,bg="#FFB6C1", text="8", padx=40, pady=20, command=lambda: Button_click(8))
my_button_9  = Button(root,bg="#FFB6C1", text="9", padx=40, pady=20, command=lambda: Button_click(9))
my_button_0  = Button(root,bg="#AB82FF", text="0", padx=40, pady=20, command=lambda: Button_click(0))

button_add = Button(root,bg="#AB82FF", text="+", padx=39, pady=20, command=Button_add)
button_mins = Button(root,bg="#AB82FF", text="-", padx=40, pady=20, command=Button_mins)
button_equal = Button(root,bg="#FF8000", text="=", padx=39, pady=57, command=button_Equal)
button_clear = Button(root,bg="#FF8000", text="clear", padx=82, pady=25, command=clear)
button_multiply = Button(root,bg="#87CEFA", text="x", padx=40, pady=20, command=Button_mult).grid(row=5, column=0)
button_devide = Button(root,bg="#87CEFA", text="/", padx=41, pady=20, command=Button_devide).grid(row=5, column=1)
my_button_1.grid(row=3, column=0)
my_button_2.grid(row=3, column=1)
my_button_3.grid(row=3, column=2)

my_button_4.grid(row=2, column=0)
my_button_5.grid(row=2, column=1)
my_button_6.grid(row=2, column=2)

my_button_7.grid(row=1, column=0)
my_button_8.grid(row=1, column=1)
my_button_9.grid(row=1, column=2)

my_button_0.grid(row=4, column=1)
button_add.grid(row=4, column=0)
button_mins.grid(row=4, column=2)
button_equal.grid(row=5, column=2, rowspan=2)
button_clear.grid(row=6, column=0, columnspan=2)


root.mainloop()