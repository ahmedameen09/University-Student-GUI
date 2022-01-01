from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk , Image
from main import checklogin


# Functions
flag = 0

def login():
    global email , password , top , flag
    email = box1.get()
    password = box2.get()
    if len(email) > 0 and len(password) > 5:
        var = checklogin(email,password)
        if var == 1 :
            loginW.destroy()
            flag = 1
        else :
            messagebox.showinfo("Invalid Login", "Email or Password are not correct!")
            flag = 0
    else :
        messagebox.showinfo("Invalid Input", "Email or Password are Empty or not completely filled")
        flag = 0
        pass

# General Configuration
loginW = Tk()
loginW.title("MRU Student System")
loginW.iconbitmap(r'C:\Users\14b007\Desktop\MRU Database Project\Logo Design\iconem.ico')
loginW.option_add("*tearOff", False)                            # for remove dashed line from ui\ux
loginW.geometry("1000x650")                                     # for default size of window
loginW.resizable(False, FALSE)                                  # for resizing of window
loginW.columnconfigure(index=0 , weight=1)
loginW.columnconfigure(index=1 , weight=2)
loginW.columnconfigure(index=2 , weight=1)
loginW.rowconfigure(index=0 , weight=1)
loginW.rowconfigure(index=1 , weight=1)
loginW.rowconfigure(index=2 , weight=1)
style = ttk.Style(loginW)

# Setting Login Frame
loginframe = ttk.Frame(loginW,padding=(20,0, 0, 10))
loginframe.grid(row=0, column=1, padx=0, pady=(50,10), sticky="nsew", rowspan=3)
loginframe.columnconfigure(index=0, weight=1)

# setting the theme
loginW.call("source", r"C:\Users\14b007\Desktop\MRU Database Project\Azure-ttk-theme-main\azure.tcl")
loginW.call("set_theme", "dark")

# setting Logo
logo = Image.open(r"C:\Users\14b007\Desktop\MRU Database Project\Logo Design\Removal-547.png")  # open image
r_logo = logo.resize((150,139), Image.ANTIALIAS)               # resizing image
F_logo = ImageTk.PhotoImage(r_logo)                            # make image photo
logolbl = Label(image=F_logo)                                  # make image as label

# setting login button
loginbtn = ttk.Button(loginframe,text = "Login",style="Accent.TButton" , width=15 , command=login ) # ttk is module from class for themed widgets

# setting Boxes Entry & Labels
box1 = ttk.Entry(loginframe)
box2 = ttk.Entry(loginframe , show="x")
lbl1 = ttk.Label(loginframe,text="Email",font=("arial" , 11 , "bold"),foreground="white")
lbl2 = ttk.Label(loginframe,text="Password",font=("arial" , 11 , "bold"),foreground="white")
lbl3 = ttk.Label(loginframe,text="Forgotten password?",font=("arial" , 10),foreground="grey")

# Setting widgets on the screen
logolbl.grid(row=0, column=1 , pady=(10,30) ,sticky=EW)
lbl1.grid(row=1 , column=0 , columnspan=1 , pady=(185,10) , padx=(190,200) , sticky=W)
box1.grid(row=2 ,column=0 , columnspan=1 , pady=(0,10) , padx=(190,200) , sticky=EW)
lbl2.grid(row=3 , column=0 , columnspan=1 , pady=(10,10) , padx=(190,200) , sticky=W)
box2.grid(row=4 , column=0 , columnspan=1 , pady=(0,20) , padx=(190,200) , sticky=EW)
lbl3.grid(row=5 , column=0 , columnspan=1 , pady=(20,10) , padx=(190,200))
loginbtn.grid(row=6 ,column=0 , columnspan=1 , pady=20 , padx=(190,200))

# Loops Running
loginW.mainloop()

#______________________________________________________________________________________________________

# Functions

def signout() :
    pass


# Window Configuration of student main

if flag == 1 :
    mainW = Tk()
    mainW.title("MISR University Student System")
    mainW.iconbitmap(r'C:\Users\14b007\Desktop\MRU Database Project\Logo Design\iconem.ico')
    mainW.option_add("*tearOff", False)
    mainW.geometry("1200x680")
    mainW.resizable(True, True)
    mainW.columnconfigure(index=0 , weight=1)
    mainW.columnconfigure(index=1 , weight=1)
    mainW.columnconfigure(index=2 , weight=1)
    mainW.columnconfigure(index=3 , weight=1)
    mainW.rowconfigure(index=0 , weight=1)
    mainW.rowconfigure(index=1 , weight=1)
    mainW.rowconfigure(index=2 , weight=1)
    mainW.rowconfigure(index=3 , weight=1)
    sizegrip = ttk.Sizegrip(mainW)
    sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))
    style = ttk.Style(mainW)

    # setting the theme
    mainW.call("source", r"C:\Users\14b007\Desktop\MRU Database Project\Azure-ttk-theme-main\azure.tcl")
    mainW.call("set_theme", "dark")

    # Frames
    # frame['padding'] = (left, top, right, bottom)
    # frame['padding'] allows you to add extra space around the inside of the frame.

    frame_0 = ttk.LabelFrame(mainW,height=550,width=250,borderwidth=5,text="Student Info",labelanchor=N)
    frame_1 = ttk.Frame(mainW, height=200, width=200, borderwidth=5)
    frame_2 = ttk.Frame(mainW,height=200,width=200,borderwidth=5)
    frame_3 = ttk.Frame(mainW,height=200,width=200,borderwidth=5)
    frame_4 = ttk.Frame(mainW, height=200, width=200, borderwidth=5)
    frame_5 = ttk.Frame(mainW,height=200,width=200,borderwidth=5)
    frame_6 = ttk.Frame(mainW,height=200,width=200,borderwidth=5)
    frame_7 = ttk.LabelFrame(mainW,height=200 ,width=800,borderwidth=5,text="MRU",labelanchor=N)

    # Griding on Screen
    # padx and pady allows you to add extra space around the outside of the frame

    frame_0.grid(row=1,rowspan=4,column=0,sticky="W",padx=(60,0),pady=(10,10))
    frame_1.grid(row=1,column=1,sticky="WS")
    frame_2.grid(row=1,column=2,sticky="WS")
    frame_3.grid(row=1,column=3,sticky="WS")
    frame_4.grid(row=2,column=1,sticky="WS")
    frame_5.grid(row=2,column=2,sticky="WS")
    frame_6.grid(row=2,column=3,sticky="WS")
    frame_7.grid(row=0,column=0,columnspan=4,sticky="WSNE",padx=(60,60),pady=(20,10))


    # Frame_1 Widgets setting

    img1 = Image.open(r"C:\Users\14b007\Desktop\MRU Database Project\Pngs\Announcment.png")
    r_img1 = img1.resize((160,160), Image.ANTIALIAS)
    F_img1 = ImageTk.PhotoImage(r_img1)
    img1_lbl = Label(frame_1,image=F_img1)
    btn1 = ttk.Button(frame_1,text = "Announcement")
    img1_lbl.grid(pady=(0,10),padx=10)
    btn1.grid()


    # Frame_2 Widgets setting

    img2 = Image.open(r"C:\Users\14b007\Desktop\MRU Database Project\Pngs\Registration.png")
    r_img2 = img2.resize((160,160), Image.ANTIALIAS)
    F_img2 = ImageTk.PhotoImage(r_img2)
    img2_lbl = Label(frame_2,image=F_img2)
    btn2 = ttk.Button(frame_2,text = "Registration",width=12)
    img2_lbl.grid(pady=(0,10),padx=10)
    btn2.grid()


    # Frame_3 Widgets setting

    img3 = Image.open(r"C:\Users\14b007\Desktop\MRU Database Project\Pngs\kindpng_211349.png")
    r_img3 = img3.resize((160,160), Image.ANTIALIAS)
    F_img3 = ImageTk.PhotoImage(r_img3)
    img3_lbl = Label(frame_3,image=F_img3)
    btn3 = ttk.Button(frame_3,text = "Results",width=12)
    img3_lbl.grid(pady=(0,10),padx=10)
    btn3.grid()


    # Frame_4 Widgets setting

    img4 = Image.open(r"C:\Users\14b007\Desktop\MRU Database Project\Pngs\kindpng_3179993.png")
    r_img4 = img4.resize((160,160), Image.ANTIALIAS)
    F_img4 = ImageTk.PhotoImage(r_img4)
    img4_lbl = Label(frame_4,image=F_img4)
    btn4 = ttk.Button(frame_4,text = "Departments",width=12)
    img4_lbl.grid(pady=(0,10),padx=10)
    btn4.grid()


    # Frame_5 Widgets setting

    img5 = Image.open(r"C:\Users\14b007\Desktop\MRU Database Project\Pngs\1679522.png")
    r_img5 = img5.resize((160,160), Image.ANTIALIAS)
    F_img5 = ImageTk.PhotoImage(r_img5)
    img5_lbl = Label(frame_5,image=F_img5)
    btn5 = ttk.Button(frame_5,text = "Regulations",width=12)
    img5_lbl.grid(pady=(0,10),padx=10)
    btn5.grid()


    # Frame_6 Widgets setting

    img6 = Image.open(r"C:\Users\14b007\Desktop\MRU Database Project\Pngs\communication-icon-png-16.png")
    r_img6 = img6.resize((160,160), Image.ANTIALIAS)
    F_img6 = ImageTk.PhotoImage(r_img6)
    img6_lbl = Label(frame_6,image=F_img6)
    btn6 = ttk.Button(frame_6,text = "MRU Social",width=12)
    img6_lbl.grid(pady=(0,10),padx=10)
    btn6.grid()

    # Sign-out Button

    # btn0 = ttk.Button(frame_0,text="Sign-out",style="Accent.TButton" ,command=signout)
    # btn0.grid(row=2,pady=(300,100))
    mainW.mainloop()
