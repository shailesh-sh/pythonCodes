import tkinter as tk
from tkinter import messagebox

def clrUsrname(event):
	if entryPassword.get()=="":
		entryPassword.insert(0,"Enter Password")
	entryUsrname.delete(0, "end")

def clrPassword(event):
	if entryUsrname.get()=="":
		entryUsrname.insert(0,"Enter Username or Email")
	entryPassword.delete(0, "end")

def clrCPassword(event):
	if entryPassword.get()=="":
		entryPassword.insert(0,"Enter Password")
	if entryUsrname.get()=="":
		entryUsrname.insert(0,"Enter Username or Email")
	entryCPassword.delete(0, "end")

def Login():
	messagebox.showwarning("Message","This is just a Demo")

def Register():
	global root1,entryUsrname,entryPassword,entryCPassword
	try:
		root1.destroy()
		root.destroy()
	except:
		print("Register")
	finally:	
		root1 = tk.Tk()
		root1.title("Register")
		labelUsrname = tk.Label(root1, text="Username/Email")
		labelUsrname.grid(column=1, row=1)
		entryUsrname = tk.Entry(root1, width=25)
		entryUsrname.insert(0, "Enter Username or Email")
		entryUsrname.bind("<Button>", clrUsrname)
		entryUsrname.grid(column=3, row=1)

		labelPassword = tk.Label(root1, text="Password")
		labelPassword.grid(column=1, row=2)
		entryPassword = tk.Entry(root1, width=25)
		entryPassword.insert(0, "Enter Password")
		entryPassword.bind("<Button>", clrPassword)
		entryPassword.grid(column=3, row=2)

		labelCPassword = tk.Label(root1, text="Confirm Password")
		labelCPassword.grid(column=1, row=3)
		entryCPassword = tk.Entry(root1, width=25)
		entryCPassword.insert(0, "Confirm Password")
		entryCPassword.bind("<Button>", clrCPassword)
		entryCPassword.grid(column=3, row=3)

		labelSpace = tk.Label(root1,text="",width=10)
		labelSpace.grid(column=2, row=1)

		labelSpace1 = tk.Label(root1,text="")
		labelSpace1.grid(row=4)

		btnLogin = tk.Button(root1, text="Login", relief="groove",width=5, command=LoginScreen)
		btnLogin.grid(row=5, column=2)

		btnRegister = tk.Button(root1, text="Register", relief="groove",width=5,command=Login)
		btnRegister.grid(row=5, column=3)	
		root1.mainloop()

def LoginScreen():
	global root,entryUsrname,entryPassword
	try:
		root.destroy()
		root1.destroy()
	except:
		print("First Time")
	finally:	
		root = tk.Tk()
		root.title("Login")
		labelUsrname = tk.Label(root, text="Username/Email")
		labelUsrname.grid(column=1, row=1)
		entryUsrname = tk.Entry(root, width=25)
		entryUsrname.insert(0, "Enter Username or Email")
		entryUsrname.bind("<Button>", clrUsrname)
		entryUsrname.grid(column=3, row=1)

		labelPassword = tk.Label(root, text="Password")
		labelPassword.grid(column=1, row=2)
		entryPassword = tk.Entry(root, width=25)
		entryPassword.insert(0, "Enter Password")
		entryPassword.bind("<Button>", clrPassword)
		entryPassword.grid(column=3, row=2)

		labelSpace = tk.Label(root,text="",width=10)
		labelSpace.grid(column=2, row=1)

		labelSpace1 = tk.Label(root,text="")
		labelSpace1.grid(row=3)

		btnLogin = tk.Button(root, text="Login", relief="groove",width=5, command=Login)
		btnLogin.grid(row=4, column=2)

		btnRegister = tk.Button(root, text="Register", relief="groove",width=5, command=Register)
		btnRegister.grid(row=4, column=3)
		root.mainloop()


LoginScreen()
