from Tkinter import  *
import Tkinter, Tkconstants, tkFileDialog
import os    
from my import my
from decrypt import decrypt
def Enc():
	my()
def Dec():
	decrypt()
def index():
	root = Tk()
	frame = Frame(root)
	frame.pack()

	button = Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
	button.pack(side=LEFT)
	slogan = Button(frame,
                   text="encrypt",
                   command=Enc)
	slogan.pack(side=LEFT)
	decr=Button(frame,text="Decrypt",command=Dec)
	decr.pack(side=LEFT)
	root.mainloop()
