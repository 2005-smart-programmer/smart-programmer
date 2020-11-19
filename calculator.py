# So let's make a simple calculator using Tkinter, GUI and obviously Python

# So let's jump right into it

# So to build the calculator we need to import tkinter at first and then do the required things

from tkinter import *

# Now we must have a screen where the app will be built

screen = Tk()

# At first we need an input which is main here, chill out everything is main i.e., important

entry = Entry(screen, width=50, borderwidth=5)

# Now we have our input, let's check it out

# Now I want to rename it as Calculator

screen.title("Calculator")

# Now we should have the buttons i.e., 0,1... upto 9 and +,-,/,* and clear

# Let's do with the functions first viz., add, multiply, divide and subtract and the equals to buttons


def button_click(number):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current) + str(number))

'''
def entry_cleared():
    new = entry.get()
    entry.delete(END,END)
'''    

def clear_everything():
    entry.delete(0,END)



def button_add():
    numbers = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(numbers)
    entry.delete(0,END)



def button_subtract():
    numbers = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(numbers)
    entry.delete(0,END)



def button_multiply():
    numbers = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(numbers)
    entry.delete(0,END)


def button_divide():
    numbers = entry.get()
    global f_num
    global math
    math = "division"
    f_num = int(numbers)
    entry.delete(0,END)

def calculate_the_result():
    second_number = entry.get()
    entry.delete(0,END)
    if math == "addition":
        entry.insert(0, f_num + int(second_number))
    

    elif math == "subtraction":
        entry.insert(0, f_num - int(second_number))
    

    elif math == "multiplication":
        entry.insert(0, f_num * int(second_number))
    

    elif math == "division":
        entry.insert(0, f_num / int(second_number))
    
    

# Here are our buttons 
    
button8 = Button(screen,text=7, padx=40, pady=20, command=lambda: button_click(7))
button9 = Button(screen,text=8, padx=40, pady=20, command=lambda: button_click(8))
button10 = Button(screen,text=9, padx=40, pady=20, command=lambda: button_click(9))
button5 = Button(screen,text=4, padx=40, pady=20, command=lambda: button_click(4))
button6 = Button(screen,text=5, padx=40, pady=20, command=lambda: button_click(5))
button7 = Button(screen,text=6, padx=40, pady=20, command=lambda: button_click(6))
button2 = Button(screen,text=1, padx=40, pady=20, command=lambda: button_click(1))
button3 = Button(screen,text=2, padx=40, pady=20, command=lambda: button_click(2))
button4 = Button(screen,text=3, padx=40, pady=20, command=lambda: button_click(3))
button1 = Button(screen,text=0, padx=40, pady=20, command=lambda: button_click(0))
button11 = Button(screen,text='+', padx=40, pady=20, command=button_add)
button12 = Button(screen,text='-', padx=40, pady=20, command=button_subtract)
button13 = Button(screen,text='/', padx=40, pady=20, command=button_divide)
button14 = Button(screen,text='*', padx=40, pady=20, command=button_multiply)
button15 = Button(screen,text="clear", padx=40, pady=20, command=clear_everything)
button16 = Button(screen, text="=",padx=40, pady=20, command=calculate_the_result)



# Now we must pack all of them into the screen

entry.grid(row=0, column=0, columnspan=3, pady=40)
button8.grid(row=1, column=0)
button9.grid(row=1, column=1)
button10.grid(row=1, column=2)
button5.grid(row=2, column=0)
button6.grid(row=2, column=1)
button7.grid(row=2, column=2)
button2.grid(row=3, column=0)
button3.grid(row=3, column=1)
button4.grid(row=3, column=2)
button1.grid(row=4, column=0)
button11.grid(row=4, column=1)
button12.grid(row=4, column=2,columnspan=2)
button13.grid(row=5, column=0)
button14.grid(row=5, column=1)
button15.grid(row=6, column=0)
button16.grid(row=6,column=1)


# Now another important and last thing is that the loop must run infinitely. So let's do thatd


screen.mainloop()

# So here is our Calculator app 
# There are no designs in this app because I'm a beginner and have just started to learn Tkinter yesterday


