from tkinter import *

root = Tk()
root.title("Saurabh's Calculator")

e = Entry(width=30, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

num1 = ""
num2 = ""
last_operator = ""
last_equal = False

def button_click(number):
    global last_equal
    current = ""
    if last_equal == TRUE:
        last_equal = FALSE
        current = number
        e.delete(0, END)
        e.insert(0, str(current))
    else:
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))

def button_clean():
    global num1, num2, last_operator, last_equal
    e.delete(0, END)
    num1 = ""
    num2 = ""
    last_operator = ""
    last_equal = FALSE

def button_operator(operator, last_operator1):
    #print(last_operator1)
    global last_operator, num1
    if last_operator1 == "":
        num1= e.get()
        #print(str(num1))
        e.delete(0, END)
        last_operator = operator

def button_equal(last_operator1):
    global num1, num2, last_equal
    global last_operator
    if last_operator1 != "":
        num2 = e.get()
    e.delete(0, END)
    if last_operator == "plus":
        e.insert(0, float(num1)+float(num2))
    elif last_operator == "minus":
        e.insert(0, float(num1)-float(num2))
    elif last_operator == "multiply":
        e.insert(0, float(num1) * float(num2))
    elif last_operator == "divide":
        try:
            e.insert(0, float(num1) / float(num2))
        except ZeroDivisionError:
            e.insert("ERR: DIV By Zero")
            button_clean()
    last_operator=""
    last_equal = TRUE



button_1 = Button(root, padx=30, pady=20, command=lambda: button_click(1), text="1")
button_2 = Button(root, padx=30, pady=20, command=lambda: button_click(2), text="2")
button_3 = Button(root, padx=30, pady=20, command=lambda: button_click(3), text="3")
button_4 = Button(root, padx=30, pady=20, command=lambda: button_click(4), text="4")
button_5 = Button(root, padx=30, pady=20, command=lambda: button_click(5), text="5")
button_6 = Button(root, padx=30, pady=20, command=lambda: button_click(6), text="6")
button_7 = Button(root, padx=30, pady=20, command=lambda: button_click(7), text="7")
button_8 = Button(root, padx=30, pady=20, command=lambda: button_click(8), text="8")
button_9 = Button(root, padx=30, pady=20, command=lambda: button_click(9), text="9")
button_0 = Button(root, padx=30, pady=20, command=lambda: button_click(0), text="0")
button_plus = Button(root, padx=30, pady=20, command=lambda: button_operator("plus", last_operator), text="+")
button_minus = Button(root, padx=30, pady=20, command=lambda:button_operator("minus", last_operator), text="-")
button_multiply = Button(root, padx=30, pady=20, command=lambda: button_operator("multiply", last_operator), text="X")
button_divide = Button(root, padx=30, pady=20, command=lambda: button_operator("divide", last_operator), text="/")
button_equals = Button(root, pady=20,  padx=110, text="=", command=lambda: button_equal(last_operator))
button_clear = Button(root, padx=30, pady=20, text="C", command=lambda: button_clean())

button_1.grid(row=1, column="0")
button_2.grid(row=1, column="1")
button_3.grid(row=1, column="2")
button_4.grid(row=2, column="0")
button_5.grid(row=2, column="1")
button_6.grid(row=2, column="2")
button_7.grid(row=3, column="0")
button_8.grid(row=3, column="1")
button_9.grid(row=3, column="2")
button_0.grid(row=4, column="0")
button_plus.grid(row="4", column="1")
button_minus.grid(row="4", column="2")
button_equals.grid(row="6", column="0", columnspan ="3")
button_clear.grid(row="5", column="0")
button_multiply.grid(row="5", column="1")
button_divide.grid(row="5", column="2")


#root.pack()
root.mainloop()
