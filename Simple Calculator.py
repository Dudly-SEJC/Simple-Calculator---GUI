import tkinter
from tkinter import *
from PIL import Image, ImageTk
root = Tk()
# set the background colour of GUI window
#gui.configure(background="light green")
# set the title of GUI window
root.title("Simple Calculator")
# set the configuration of GUI window
root.geometry("240x150")
# StringVar() is the variable class
# we create an instance of this class
#equation = StringVar()
# create the text entry box for
# showing the expression .
#expression_field = Entry(root, textvariable=equation)
#the code above can also be written as:
#expression_field = Entry(root, textvariable=equation, width=50)
#Entry doesn't have height option. We need to do it by changing font size.
#Add, font=('Arial 24')) in the code above.
# grid method is used for placing the widgets at respective positions
#in table like structure .
#expression_field.grid(columnspan=4, ipadx=70)
# create a Buttons and place at a particular
# location inside the root window .
# when user press the button, the command or
# function affiliated to that button is executed .
button1 = Button(root, text=' 100 ', fg='black', bg='red',height=1, width=7)
button1.grid(row=2, column=0)
#command=lambda: press(1)
button2 = Button(root, text=' 2 ', fg='black', bg='red', height=1, width=7)
button2.grid(row=2, column=1)
button3 = Button(root, text=' 3 ', fg='black', bg='red',height=1, width=7)
button3.grid(row=2, column=2)
button4 = Button(root, text=' 4 ', fg='black', bg='red',height=1, width=7)
button4.grid(row=3, column=0)
button5 = Button(root, text=' 5 ', fg='black', bg='red', height=1, width=7)
button5.grid(row=3, column=1)
button6 = Button(root, text=' 6 ', fg='black', bg='red',
height=1, width=7)
button6.grid(row=3, column=2)
button7 = Button(root, text=' 7 ', fg='black', bg='red',
height=1, width=7)
button7.grid(row=4, column=0)
button8 = Button(root, text=' 8 ', fg='black', bg='red',
height=1, width=7)
button8.grid(row=4, column=1)
button9 = Button(root, text=' 9 ', fg='black', bg='red',
height=1, width=7)
button9.grid(row=4, column=2)
button0 = Button(root, text=' 0 ', fg='black', bg='red',
height=1, width=7)
button0.grid(row=5, column=0)
plus = Button(root, text=' + ', fg='black', bg='red',
height=1, width=7)
plus.grid(row=2, column=3)
minus = Button(root, text=' - ', fg='black', bg='red',
height=1, width=7)
minus.grid(row=3, column=3)
root.mainloop()
