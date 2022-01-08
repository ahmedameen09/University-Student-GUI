import mysql.connector
from tkinter import messagebox


def checklogin(email,password):
    try :
        mydb = mysql.connector.connect(host="localhost", user="admin", passwd="123456", database="accounts")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT Email,Password FROM accounts.students WHERE Email= '%s'" %email)
        result = mycursor.fetchone()
    except :
        return -1

    if result != None : #check the value in result not null
        if email == result[0] and password == result[1]:
            return 1
    else:
        return 0


def checklogin2(email,password):
    try :
        mydb = mysql.connector.connect(host="localhost", user="admin", passwd="123456", database="accounts")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT Email,Password FROM accounts.admins WHERE Email= '%s'" %email)
        result = mycursor.fetchone()
    except :
        return -1

    if result != None : #check the value in result not null
        if email == result[0] and password == result[1]:
            return 1
    else:
        return 0


def add_saccount_db(email,password,id):
    try :
        mydb = mysql.connector.connect(host="localhost", user="admin", passwd="123456", database="accounts")
        mycursor = mydb.cursor()
        record = (email,password,id)
        mycursor.execute( "INSERT INTO accounts.students (Email, Password, SID) VALUES ('%s','%s','%s')" %record)
        mydb.commit()
        messagebox.showinfo("Account Made", "Account had been Recorded Successfully!")
    except:
        messagebox.showerror("Database Error", "Please Try Again Later")


def r_saccount_db(email):
    mydb = mysql.connector.connect(host="localhost", user="admin", passwd="123456", database="accounts")
    mycursor = mydb.cursor()
    mycursor.execute("DELETE * FROM accounts.students WHERE Email= '%s'" %email)
    mycursor.close()
    mydb.close()

def Re_saccount_db(email,password):
    mydb = mysql.connector.connect(host="localhost", user="admin", passwd="123456", database="accounts")
    mycursor = mydb.cursor()
    result = (password,email)
    mycursor.execute("UPDATE accounts.students SET Password ='%s' WHERE Email ='%s' " %result)
    mycursor.close()
    mydb.close()


def add_adm_db(id,ssn,name,address,gender,salary,grad,job,phone):
    try :
        mydb = mysql.connector.connect(host="localhost", user="admin", passwd="123456", database="mru")
        mycursor = mydb.cursor()
        record = (id,ssn,name,phone,address,gender,salary,grad,job)
        mycursor.execute("INSERT INTO mru.adm VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" %record)
        mydb.commit()
        mycursor.close()
        mydb.close()
        messagebox.showinfo("Record Made", "Administrator had been Recorded Successfully!")
    except:
        messagebox.showerror("Database Error", "Please Try Again Later")



def search_adm_db(id):
    try:
        mydb = mysql.connector.connect(host="localhost", user="admin", passwd="123456", database="mru")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM mru.adm WHERE aid = '%s'" % id)
        result = mycursor.fetchone()
        if result != None:
           messagebox.showinfo("Administrator result", result)
        else :
           messagebox.showerror("Invalid Search", "Entry not Found Stop Playing !")
    except:
        messagebox.showerror("Database Error", "Please Try Again Later")


def search_prof_db(id):
    try:
        mydb = mysql.connector.connect(host="localhost", user="admin", passwd="123456", database="mru")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM mru.prof WHERE pid = '%s'" % id)
        result = mycursor.fetchone()
        if result != None:
           messagebox.showinfo("Professors result", result)
        else :
           messagebox.showerror("Invalid Search", "Entry not Found Stop Playing !")
    except:
        messagebox.showerror("Database Error", "Please Try Again Later")

def search_dem_db(id):
    try:
        mydb = mysql.connector.connect(host="localhost", user="admin", passwd="123456", database="mru")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM mru.dem WHERE did = '%s'" % id)
        result = mycursor.fetchone()
        if result != None:
           messagebox.showinfo("Professors result", result)
        else :
           messagebox.showerror("Invalid Search", "Entry not Found Stop Playing !")
    except:
        messagebox.showerror("Database Error", "Please Try Again Later")

def add_student_db(id,ssn,name,address,gender,GPA,classy,units,phone):
    try:
        mydb = mysql.connector.connect(host="localhost", user="admin", passwd="123456", database="mru")
        mycursor = mydb.cursor()
        record = (id,ssn,name,phone,address,gender,classy,units,GPA)
        mycursor.execute("INSERT INTO mru.students VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" %record)
        mydb.commit()
        mycursor.close()
        mydb.close()
        messagebox.showinfo("Account Made", "Student has been Recorded Successfully!")
    except:
        messagebox.showerror("Database Error", "Please Try Again Later")


def search_student_db(id):
    try:
        mydb = mysql.connector.connect(host="localhost", user="admin", passwd="123456", database="mru")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM mru.students WHERE sid = '%s'" % id)
        result = mycursor.fetchone()
        if result != None:
           messagebox.showinfo("Professors result", result)
        else :
           messagebox.showerror("Invalid Search", "Entry not Found Stop Playing !")
    except:
        messagebox.showerror("Database Error", "Please Try Again Later")


def search_s_result_db(id):
    try:
        mydb = mysql.connector.connect(host="localhost", user="admin", passwd="123456", database="mru")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM mru.finished WHERE sid = '%s'" % id)
        result = mycursor.fetchone()
        if result != None:
            messagebox.showinfo("Professors result", result)
        else:
            messagebox.showerror("Invalid Search", "Student has no results Yet !")
    except:
        messagebox.showerror("Database Error", "Please Try Again Later")
