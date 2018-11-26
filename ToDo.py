import tkinter 
import random
from tkinter import messagebox

root = tkinter.Tk()
root.configure(bg="white")
root.title("Python Project")
root.geometry("325x275")

tasks = []

def update_listbox():
    clear_listbox()
    for task in tasks:
        ltasks.insert("end",task)

def clear_listbox():
    ltasks.delete(0,"end")

def add_task():
#    clear_listbox()
    task = txt_input.get()
    if task !="":
        tasks.append(task)
        update_listbox()
    else:
        display["text"] = "Enter Valid Task"
        messagebox.showwarning("Warning","Enter Valid Task")
    txt_input.delete(0,"end")

def del_all():
    global tasks
    confirmed = messagebox.askyesno("Confirm","Do you really want to delete all?")
    if confirmed:
        tasks = []
        update_listbox()

def del_one():
    task = ltasks.get("active")
    if task in tasks:
        tasks.remove(task)
    update_listbox()

def sort_asc():
    tasks.sort()
    update_listbox()

def sort_desc():
    tasks.sort()
    tasks.reverse()
    update_listbox()

def choose_random():
    task = random.choice(tasks)
    display["text"] = task

def show_number_of_tasks():
    number_of_tasks = len(tasks)
    msg = "Number of tasks: %s"%number_of_tasks
    display["text"] = msg


title = tkinter.Label(root,text="To-Do List",bg="gray")
title.grid(row=0,column=0)

display = tkinter.Label(root,text="",bg="white")
display.grid(row=0,column=1)

txt_input = tkinter.Entry(root,width=25,bg="lightgreen")
txt_input.grid(row=1,column=1)

btn_add_task = tkinter.Button(root, text="Add Task", fg="white", bg="gray", command=add_task)
btn_add_task.config(width=15)
btn_add_task.grid(row=1,column=0)

btn_del_all= tkinter.Button(root, text="Delete All", fg="white", bg="gray", command=del_all)
btn_del_all.config(width=15)
btn_del_all.grid(row=2,column=0)

btn_del_one= tkinter.Button(root, text="Delete", fg="white", bg="gray", command=del_one)
btn_del_one.config(width=15)
btn_del_one.grid(row=3,column=0)

btn_sort_asc= tkinter.Button(root, text="Sort Ascending", fg="white", bg="gray", command=sort_asc)
btn_sort_asc.config(width=15)
btn_sort_asc.grid(row=4,column=0)

btn_sort_desc= tkinter.Button(root, text="Sort Descending", fg="white", bg="gray", command=sort_desc)
btn_sort_desc.config(width=15)
btn_sort_desc.grid(row=5,column=0)

btn_choose_random= tkinter.Button(root, text="Choose Random", fg="white", bg="gray", command=choose_random)
btn_choose_random.config(width=15)
btn_choose_random.grid(row=6,column=0)

btn_number_of_tasks= tkinter.Button(root, text="Number Of Tasks", fg="white", bg="gray", command=show_number_of_tasks)
btn_number_of_tasks.config(width=15)
btn_number_of_tasks.grid(row=7,column=0)

btn_exit= tkinter.Button(root, text="Exit", fg="white", bg="gray", command=exit)
btn_exit.config(width=15)
btn_exit.grid(row=8,column=0)


ltasks = tkinter.Listbox(root)
ltasks.grid(row=2,column=1,rowspan=7)

root.mainloop()
