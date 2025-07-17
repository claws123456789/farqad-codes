from tkinter import *

# Create Window
root = Tk()
root.title('Login App')
root.geometry('400x400')
def farqad():
	# Setting up Top Window
	top = Toplevel()
	top.geometry("180x100")
	top.title("toplevel")
	# Adding a label widget to Top Window
	l2 = Label(top, text = "This is toplevel window")
	l2.pack()

	top.mainloop()
lbl = Label(root,text = "this is a root window",bg = "yellow")
btn = Button(root,text = "click here to open the other window",command = farqad)
lbl.pack()
btn.pack()
root.mainloop()




