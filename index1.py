from tkinter import *
import sqlite3
from index import index
import bluetooth
import tkMessageBox
 
def Bluelogged():
	target_name = USERNAME.get()
	target_address = None

	nearby_devices = bluetooth.discover_devices()

	for bdaddr in nearby_devices:
    		if target_name == bluetooth.lookup_name( bdaddr ):
        		target_address = bdaddr
        		break
		print target_name
	PASSWORD.set(target_address)	
	Login()
def Database():
        global conn, cursor
        conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")       
        cursor.execute("SELECT * FROM `member` WHERE `username` = 'Galaxy S7' AND  `password` = '60:8E:08:42:B7:13'")
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO `member` (username, password) VALUES('Galaxy S7', '60:8E:08:42:B7:13')")
            conn.commit()
def Login(event=None):
        Database()
        if USERNAME.get() == "" or PASSWORD.get() == "":
            lbl_text.config(text="Please complete the required field!", fg="red")
        else:
            cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
            if cursor.fetchone() is not None:
		index()
            else:
                lbl_text.config(text="Invalid username or password", fg="red")

                USERNAME.set("")
                PASSWORD.set("")   
        cursor.close()
        conn.close()
     
def HomeWindow():
        global Home
        root.withdraw()
        Home = Toplevel()
        Home.title("BLUETOOTH")
        width = 600
        height = 500
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        root.resizable(0, 0)
        Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
        lbl_home = Label(Home, text="Successfully Login!", font=('times new roman', 20)).pack()
        btn_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)
     
def Back():
        Home.destroy()
        root.deiconify()

root = Tk()
    
root.title("Project Blue")
    
width = 400
    
height = 280
    
screen_width = root.winfo_screenwidth()
    
screen_height = root.winfo_screenheight()
    
x = (screen_width/2) - (width/2)
    
y = (screen_height/2) - (height/2)
    
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    
root.resizable(0, 0)
Database()
    #==============================VARIABLES======================================
USERNAME = StringVar()
PASSWORD = StringVar()
     
    #==============================FRAMES=========================================
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)
     
    #==============================LABELS=========================================
lbl_title = Label(Top, text = "Project Bluetooth", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15)
    
lbl_username.grid(row=0, sticky="e")
    

    
lbl_text = Label(Form)
    
lbl_text.grid(row=2, columnspan=2)
     
    #==============================ENTRY WIDGETS==================================
    
username = Entry(Form, textvariable=USERNAME, font=(14))
    
username.grid(row=0, column=1)
    

     
    #==============================BUTTON WIDGETS=================================
    
btn_login = Button(Form, text="Login Via Bluetooth", width=45, command=Bluelogged)
 
btn_login.grid(pady=25, row=3, columnspan=2)
    
btn_login.bind('<Return>', Login)


    #==============================INITIALIATION==================================
if __name__ == '__main__':
    root.mainloop()
