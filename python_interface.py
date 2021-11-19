# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 15:50:49 2021

@author: PaulineM
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
        
from tkinter import *
import subprocess
import re

window = Tk()
window.geometry("400x200")
window.title("Welcome")

#FUNCTIONS
#change background color
def color():
    btn['bg'] = "yellow"

#open file explorer
def file():
    subprocess.Popen(r'explorer /select,"C:\path\of\folder\file"')

#enlarge screen size    
def fullScreen():
    #window.attributes('-fullscreen', True)
    window.geometry("950x650")
 
#display message box
def message():
    messagebox.showinfo("Basic Example", "This will display a message !")

#display selected text    
def checkbox():
    if(checked.get() == 1):
        messagebox.showinfo("Your choice", "Display Text 1")
    if(checked.get() == 2):
        messagebox.showinfo("Your choice", "Display Text 2")
    if(checked.get() == 3):
         messagebox.showinfo("Your choice", "Display Text 3")

#data validation         
def formSubmit():
    
    sub_mail = str(mail_entry.get())
   
    #check if entry = str  ->r'' for 'read'
    name_regex = r'[a-zA-Z]'   #\w = [a-zA-Z]
    if(re.search(name_regex, str(name_entry.get()))): #preg_match
        sub_name = name_entry.get()
    else: 
        print("name = not ok")
        messagebox.showerror("Input error", "Name error")
        
    #check if entry = email
    mail_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.search(mail_regex, str(mail_entry.get()))):
        sub_mail = mail_entry.get()
    else: 
        print("mail = not ok")
        messagebox.showerror("Input error", "Mail error")
    
    #check if entry = num + min age
    if(age_entry.get().isdigit() and int(age_entry.get()) > 15):
        sub_age = age_entry.get()
    else: 
        print("Error : age = not ok") 
        messagebox.showerror("Input error", "Age error")          
    
    #register datas in a file
    form_datas = "Your username : " + sub_name +  "\nYour email : " + sub_mail +  "\nYour age : " + sub_age
    file = open("myfile.txt", "w")
    file.write(form_datas)
    messagebox.showinfo("Validated form", "Form well registered")  
       

#BTN
btn = Button(window, text="Turn yellow", command=color)
btn.grid(row = 0, column = 1, pady = 10, padx = 10)

closing_btn = Button(window, text="Close", command=window.destroy, bg = "lightcoral")
closing_btn.grid(row = 0, column = 4, pady = 2)


#MENU
menubar = Menu(window)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="File", command=file)
menu1.add_command(label="Full-screen", command=fullScreen)
menu1.add_command(label="Message", command=message)
menubar.add_cascade(label="Menu", menu=menu1)

menu2 = Menu(menubar, tearoff=2)
menu2.add_command(label="Item 1")
menu2.add_command(label="Item 2")
menu2.add_separator()
menu2.add_command(label="Item 3")
menubar.add_cascade(label="Menu", menu=menu2)

window.config(menu=menubar)

checked = IntVar() #IntVar = variable de contrôle (enregistre état)

#`CHECKBOXES
choice1 = Checkbutton(window, text="Text 1", variable=checked, onvalue=1, offvalue=0, command=checkbox)
choice1.grid(row = 3, column = 1, pady = 2)
choice2 = Checkbutton(window, text="Text 2", variable=checked, onvalue=2, offvalue=0, command=checkbox)
choice2.grid(row = 3, column = 2, pady = 2)
choice3 = Checkbutton(window, text="Text 3", variable=checked, onvalue=3, offvalue=0, command=checkbox)
choice3.grid(row = 3, column = 3, pady = 2, padx = 10)

#FORM
name_label = Label(window ,text = "Name").grid(row = 4,column = 1)
name_entry = Entry(window)
name_entry.grid(row = 4,column = 2)

mail_label = Label(window ,text = "Email").grid(row = 5,column = 1)
mail_entry = Entry(window)
mail_entry.grid(row = 5,column = 2)

age_label = Label(window ,text = "Age").grid(row = 6,column = 1)
age_entry = Entry(window)
age_entry.grid(row = 6,column = 2)

btn_submit = Button(window, text="Submit", command=formSubmit)
btn_submit.grid(row=7,column=2)

window.mainloop()
