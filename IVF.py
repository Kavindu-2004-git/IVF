import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox


def login_user():
        username=user_name.get()
        userpassword=user_password.get()
        if (username=="" or username=="user name") or(userpassword=="" or userpassword=="password"):
            tk.messagebox.showerror("Entry Error","Type user name or password correctly!!")   
        

first_window=tk.Tk()
first_window.title("Internshp Vacancy Finder")
first_window.configure(bg="white")
first_window.geometry("2000x2000") #width and height

icon_image=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\logo.jpg")
icon_photo=ImageTk.PhotoImage(icon_image)
first_window.iconphoto(False,icon_photo)#iconphoto is a variable

background_image=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\bgphoto.jpg")#open the specified jpg file
background_photo=ImageTk.PhotoImage(background_image)#convert the pil image into a formatetinker can display
label=tk.Label(first_window,image=background_photo,bg="white")#ceate a widget to display image
label.image=background_photo#prevent obstacles
label.place(x=0,y=0 ,)
label.pack()#add the label to the window

frame=tk.Frame(first_window,width=350,height=350,bg="white")
frame.place(x=500,y=390)

heading=ttk.Label(first_window,text="Sign in",font=("bold",30))
heading.place(x=610,y=390)

def on_enter(x):#x is a nomal variable
    name=user_name.get()
    if name=="user name":
      user_name.delete(0,"end")
        
def on_leave(x):
    name=user_name.get()#get eturn values
    if name=="":
        user_name.insert(0, "user name")

user_name=tk.Entry(frame,width=35,fg="black", bg="white",font=("bold",11))
user_name.place(x=30,y=80)
user_name.insert(0,"user name")

user_name.bind("<FocusIn>",on_enter)
user_name.bind("<FocusOut>",on_leave)

frame=tk.Frame(frame,width=284,height=2,bg="black").place(x=30,y=100)


def on_enter(x):
    code=user_password.get()
    if code =="password" :
       user_password.delete(0,"end")
    
    if code!= "password" or code!= "" :
      user_password.config (show="*")     

def on_leave(x):
    code=user_password.get()
    if code=="":
        user_password.insert(0, "password")
        user_password.config (show="")


user_password=tk.Entry(frame,width=35,fg="black", bg="white",font=("bold",11))
user_password.place(x=530,y=520)
user_password.insert(0,"password")


user_password.bind("<FocusIn>",on_enter)
user_password.bind("<FocusOut>",on_leave)

tk.Frame(frame,width=284,height=2,bg="black").place(x=530,y=540)


loging_button=tk.Button(first_window,text="Login",width=31,bg="#90D5FF",font=("bold",13),command=login_user)
loging_button.place(x=525,y=560)



first_window.mainloop()

