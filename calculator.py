from tkinter import *
import os
os.system('clear')

root = Tk()
root.title('Nicholas Calculator App')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

buttonStatus = {
	"addClick": False,
	"minusClick": False,
	"divClick": False,
	"multiClick": False
}


def button_click(number):
	#get what's currently in the box
	current = e.get()

	#delete what's already in the box
	e.delete(0, END)

	#insert the number clicked
	e.insert(0, str(current) + str(number)) 
	return

def button_clear():
	#delete what's already in the box
	e.delete(0, END)
	return

def button_add():
	op_flags("+")
	global	first_num
	first_num = int(e.get())
	button_clear()

	return

def button_div():
	op_flags("/")
	global	first_num
	first_num = int(e.get())
	button_clear()

	return

def button_multiply():
	op_flags("*")
	global	first_num
	first_num = int(e.get())
	button_clear()

	return


def button_minus():
	op_flags("-")
	global	first_num
	first_num = int(e.get())
	button_clear()

	return

def button_equal():
	global second_num
	second_num = int(e.get())
	printButtonStatus()

	button_clear()

	if buttonStatus["addClick"] == True:
		e.insert(0, first_num + second_num)
		reset_op_flags()

	if buttonStatus["minusClick"] == True:
		e.insert(0, first_num - second_num)
		reset_op_flags()

	if buttonStatus["divClick"] == True:
		e.insert(0, first_num / second_num)
		reset_op_flags()

	if buttonStatus["multiClick"] == True:
		e.insert(0, first_num * second_num)
		reset_op_flags()


	return

def op_flags(op):

	if op == "+":
		reset_op_flags()
		buttonStatus["addClick"] = True
		return

	if op == "-":
		reset_op_flags()
		buttonStatus["minusClick"] = True
		return

	if op == "/":
		reset_op_flags()
		buttonStatus["divClick"] = True
		return	

	if op == "*":
		reset_op_flags()
		buttonStatus["multiClick"] = True
	return

def reset_op_flags():
	for flag in buttonStatus:
		buttonStatus[flag] = False
	return

def printButtonStatus():
	print("Buttonnnn", buttonStatus)
	return


#lambda function used because we can't pass arguments into commmand i.e. no ()
button1 = Button(root, text=1, padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text=2, padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text=3, padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text=4, padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text=5, padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text=6, padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text=7, padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text=8, padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text=9, padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text=0, padx=40, pady=20, command=lambda: button_click(0))

buttonAdd = Button(root, text="+", padx=40, pady=20, command=lambda: button_add())
buttonClear = Button(root, text="Clear", padx=80, pady=20, command=lambda: button_clear())
buttonEqual = Button(root, text="=", padx=40, pady=52, command=lambda: button_equal())
buttonSubtract = Button(root, text="-", padx=40, pady=20, command=lambda: button_minus())
buttonDivide = Button(root, text="/", padx=40, pady=20, command=lambda: button_div())
buttonMultiply = Button(root, text="*", padx=40, pady=20, command=lambda: button_multiply())

#Put the buttons on the screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
    
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
    
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)


#column span is 2 since our total columnspan is 3
buttonClear.grid(row=4, column=1, columnspan=2)
buttonEqual.grid(row=5, column=2, rowspan=2)

buttonAdd.grid(row=5, column= 0)
buttonSubtract.grid(row=5, column=1)
buttonDivide.grid(row=6, column=0)
buttonMultiply.grid(row=6, column=1)





root.mainloop()