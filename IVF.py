import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


                
def opening_window():
    starting_window=tk.Tk()
    starting_window.title("Internshp Vacancy Finder")
    starting_window.configure(bg="white")
    starting_window.geometry("2000x2000")
    
    icon_image=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\logo.jpg")
    icon_photo=ImageTk.PhotoImage(icon_image)
    starting_window.iconphoto(False,icon_photo)

    label = tk.Label(starting_window, text="Welcome to Internship Vacancy Finder", font=("Arial", 24))
    label.pack(pady=200)  
      
    button1=tk.Button(starting_window,text="start",font=("bold"),command=login_window)
    button1.pack() 

    starting_window.mainloop()
    

    
def login_window():
    
    first_window=tk.Toplevel()
    first_window.title("Internshp Vacancy Finder")
    first_window.configure(bg="white")
    first_window.geometry("2000x2000") #width and height

    def login_user():
        username=user_name.get()
        userpassword= user_password.get()
        if (username=="" or username=="user name") or(userpassword=="" or userpassword=="password"):
            tk.messagebox.showerror("Entry Error","Type user name or password correctly!!")   
            return
        else:
            try:
               mydatabase=mysql.connector.connect(host="localhost",user="root",
               password="",database="internship vacancy finder")  
               mycursor=mydatabase.cursor()
               print("connected to database")
                
            except:
                print("database connection is not working")
                return
        command="use internship vacancy finder "
        mycursor.execute (command) 
            
        command="select* from user details where user name =%s and password=%s"
        mycursor.execute(command,(username,userpassword))
        result=mycursor.fetchone()
        print(result)

        if result==None:
                tk.messsagebox.showinfo("inavalied")

    icon_image=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\logo.jpg")
    icon_photo=ImageTk.PhotoImage(icon_image)
    first_window.iconphoto(False,icon_photo)#iconphoto is a variable

    background_image=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\bgphoto.jpg")#open the specified jpg file
    background_photo=ImageTk.PhotoImage(background_image)#convert the pil image into a formatetinker can display
    label=tk.Label(first_window,image=background_photo,bg="white")#ceate a widget to display image
    label.image=background_photo#prevent obstacles
    label.place(x=0,y=0 ,)
    label.pack()#add the label to the window

    frame1=tk.Frame(first_window,width=350,height=350,bg="white")
    frame1.place(x=500,y=390)

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

    user_name=tk.Entry(first_window,width=35,fg="black", bg="white",font=("bold",11))
    user_name.place(x=530,y=480)
    user_name.insert(0,"user name")

    user_name.bind("<FocusIn>",on_enter)
    user_name.bind("<FocusOut>",on_leave)

    tk.Frame(first_window,width=284,height=2,bg="black").place(x=530,y=500)


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


    user_password=tk.Entry(first_window,width=35,fg="black", bg="white",font=("bold",11))
    user_password.place(x=530,y=520)
    user_password.insert(0,"password")


    user_password.bind("<FocusIn>",on_enter)
    user_password.bind("<FocusOut>",on_leave)

    tk.Frame(first_window,width=284,height=2,bg="black").place(x=530,y=540)

    loging_button=tk.Button(first_window,text="Login",width=31,bg="#90D5FF",font=("bold",13),command=login_user,)
    loging_button.place(x=525,y=560)

    first_window.mainloop()
    
    
opening_window()
