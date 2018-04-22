import pymysql
from tkinter import*
import tkinter.messagebox
import time
import random
from PIL import Image, ImageTk
import tkinter.messagebox
import math

# Database Connection with XAMPP Mysql
conn = pymysql.connect(host='localhost',database='project',user='root',password='')
cursor = conn.cursor()

# Global Variables
global root
global r2
global r1

def message():
    tkinter.messagebox.showinfo('Window Title', 'Rajpreet Singh\nGayatri Belapurkar\nUjala Jha')

# HOME PAGE 

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.config(bg="white")
root.title("Home Page")
photo = ImageTk.PhotoImage(file="waff1.jpg")
pic = Label(root, image=photo).place(x=0,y=0,width=screen_width, height=screen_height) 

l = Label(root,text='string', bg="coral",width=screen_width,height=7).place(x=0,y=0)

home = Button(root,text='HOME', bg="coral", fg="black", font=("Arial",14), bd=0).place(x=35,y=35)

contact = Button(root,text='CONTACT', bg="coral", fg="black", font=("Arial",14), bd=0,command=message).place(x=200,y=35)

label1 = Label(root, text="Name:",font=("Arial",-20)).place(x=168, y=150)
label2 = Label(root, text="Email:",font=("Arial",-20)).place(x=168, y=200)
label3 = Label(root, text="Phone:",font=("Arial",-20)).place(x=168, y=250)
label4 = Label(root, text="Password:",font=("Arial",-20)).place(x=168, y=300)
label5 = Label(root, text="ID:",font=("Arial",-20)).place(x=168, y=350)
label6 = Label(root, text="Name:",font=("Arial",-20)).place(x=750, y=150)
label7 = Label(root, text="Password:",font=("Arial",-20)).place(x=750, y=200)


v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v5 = IntVar()
v6 = StringVar()
v7 = StringVar()

entry1 = Entry(root,textvariable=v1,font=("Arial",-20),bg="grey").place(x=350,y=150)
entry2 = Entry(root,textvariable=v2,font=("Arial",-20),bg="grey").place(x=350,y=200)
entry3 = Entry(root,textvariable=v3,font=("Arial",-20),bg="grey").place(x=350,y=250)
entry4 = Entry(root,textvariable=v4,font=("Arial",-20),bg="grey",show="*").place(x=350,y=300)
entry5 = Entry(root,textvariable=v5,font=("Arial",-20),bg="grey").place(x=350,y=350)
entry6 = Entry(root,textvariable=v6,font=("Arial",-20),bg="grey").place(x=900,y=150)
entry7 = Entry(root,textvariable=v7,font=("Arial",-20),bg="grey",show="*").place(x=900,y=200)

v = Scrollbar(root,orient=VERTICAL).pack(side=RIGHT, fill=Y)


def insert_values():
	Name = v1.get()
	Email = v2.get()
	Phone = v3.get()
	Password = v4.get()
	ID = int(v5.get())
	str = "insert into users values('%d','%s','%s','%s','%s')"
	args = (ID,Name,Email,Phone,Password)
	try:
		cursor.execute(str%args)
		conn.commit()
		tkinter.messagebox.showinfo('Window Title', 'Data Added As Follow\nName:'+Name+'\nPassword:'+Password)
	except:
		conn.rollback()
	cursor.close()
	conn.close()

def validate_admin():
    print("lol")
    Name = v6.get()
    Password = v7.get()
    if Name == "Admin":
        str = "SELECT * from `users` WHERE `Paassword` = '%s'"
        args = (Password)
        try:
            def retrieve_rows():
                    str = "select * from orders;"
                    cursor.execute(str)
                    row = cursor.fetchmany(size=10)
                    
                    b1 = Label(f1,text="ID",width='15',relief=SOLID,font=('helvetica',15, ' italic')).grid(row='0',column='0')
                    b2 = Label(f1,text="Classic Waffle",width='15',relief=SOLID,font=('helvetica',15, ' italic')).grid(row='0',column='1')
                    b3 = Label(f1,text="Peanut Butter Waffle",width='15',relief=SOLID,font=('helvetica',15, ' italic')).grid(row='0',column='2')
                    b4 = Label(f1, text="Nutella Waffle",width='15',relief=SOLID,font=('helvetica',15, ' italic')).grid(row='0',column='3')
                    b5 = Label(f1, text="Chocolate Explosion",width='15',relief=SOLID,font=('helvetica',15,' italic')).grid(row='0',column='4')
                    b6 = Label(f1,text="Roasted Walnut Waffle",width='15',relief=SOLID,font=('helvetica',15, ' italic')).grid(row='0',column='5')
                    b7 = Label(f1,text="Total",width='15',relief=SOLID,font=('helvetica',15, ' italic')).grid(row='0',column='6')
                     
                    for r in range(len(row)):
                        for i in range(7):
                            b8 = Label(f1,text=row[r][i],width='15',relief=SOLID,font=('helvetica',15, 'bold italic'))
                            b8.grid(row=r+1,column=i)
                    cursor.close()
                    conn.close()
            cursor.execute(str%args)
            conn.commit()
            if cursor.fetchone() is not None:
                root.destroy()
                
                r1=Tk()
                r1.title("Admin_page")
                f1=Frame(r1,height=1200,width=1200)
                f1.propagate(0)
                f1.grid(sticky='n')
                screen_width=r1.winfo_screenwidth()
                screen_height=r1.winfo_screenheight()
                r1.config(bg="white",width=screen_width, height=screen_height)
                retrieve_rows()
        except:
            conn.rollback()        
        r1.mainloop()

    else:
        Name = v6.get()
        Password = v7.get()

        str = "SELECT * from `users` WHERE `Paassword` = '%s' and `Name` = '%s' "
        args = (Password,Name)
        try:
            cursor.execute(str%args)
            conn.commit()
            if cursor.fetchone() is not None:
                
                r2=Tk()
                def user():
                    def exit1():
                        r2.destroy()
                        root.destroy()
                                    
                    screen_width=r2.winfo_screenwidth()
                    screen_height=r2.winfo_screenheight()
                    r2.config(bg="white",width=1900 , height=1900)

                    l=Label(r2,text='string', bg="coral",width=screen_width,height=7).place(x=0,y=0)

                    home=Button(r2,text='Logout', bg="coral", fg="black", font=("Broadway",16), bd=0,command=exit1).place(x=35,y=35)


                   
                    str1="Freshly Baked Belgium Waffle, French Vanilla Ice Cream & Whipped Cream    (150)"
                    str01="The Classic Waffle"
                    str2="Freshly Baked Belgium Waffle, Premium Chocolate Ice Cream, Whipped Cream & Peanut Butter    (170)"
                    str02="The Peanut Butter Waffle"
                    str3="Freshly Baked Belgium Waffle, French Vanilla Ice Cream, Whipped Cream & Nutella Chocolate    (160)"
                    str03="The Nutella Waffle"
                    str4="Freshly Baked Belgium Waffle, Premium Chocolate Ice Cream, Whipped Cream & Loads of Chocolate    (160)"
                    str04="The Chocolate Explosion"
                    str5="Freshly Baked Belgium Waffle, Premium Chocolate Ice Cream, Whipped Cream, Chocolate & Walnuts    (170)"
                    str05="The Roasted Walnut Waffle"

                    b1 = Label(r2,text=str01+"\n"+str1,font=("Bookman Old Style",15), bg="white").place(x=100,y=150)
                    b2 = Label(r2,text=str02+"\n"+str2,font=('Bookman Old Style',15),bg="white").place(x=100,y=250)
                    b3 = Label(r2, text=str03+"\n"+str3,font=('Bookman Old Style',15),bg="white").place(x=100,y=350)
                    b4 = Label(r2, text=str04+"\n"+str4,font=('Bookman Old Style',15),bg="white").place(x=100,y=450)
                    b5 = Label(r2,text=str05+"\n"+str5,font=('Bookman Old Style',15),bg="white").place(x=100,y=550)
                    b6 = Label(r2,text="ID",font=('Bookman Old Style',15),bg="white").place(x=800,y=650)
                    p1 = StringVar(r2)
                    p2 = StringVar(r2)
                    p3 = StringVar(r2)
                    p4 = StringVar(r2)
                    p5 = StringVar(r2)
                    p6 = StringVar(r2)
                    total = IntVar(r2)

                    b7 = Entry(r2,textvariable=p1, bg="coral", fg="black", font=("Bookman Old Style",14), bd=0)
                    b7.place(x=1200,y=150)
                    b8 = Entry(r2,textvariable=p2, bg="coral", fg="black", font=("Bookman Old Style",14), bd=0).place(x=1200,y=250)
                    b9 = Entry(r2,textvariable=p3, bg="coral", fg="black", font=("Bookman Old Style",14), bd=0).place(x=1200,y=350)
                    b10 = Entry(r2,textvariable=p4, bg="coral", fg="black", font=("Bookman Old Style",14), bd=0).place(x=1200,y=450)
                    b11 = Entry(r2,textvariable=p5, bg="coral", fg="black", font=("Bookman Old Style",14), bd=0).place(x=1200,y=550)
                    b12 = Entry(r2,textvariable=p6, bg="coral", fg="black", font=("Bookman Old Style",14), bd=0).place(x=850,y=650)

                     
                    def insert():
                        q = b7.get()
                        w = p2.get()
                        e = p3.get()
                        r = p4.get()
                        t = p5.get()
                        y = p6.get()
                        total = (150*int(q))+(160*int(w))+(170*int(e))+(160*int(r))+(170*int(t))
                        str = "insert into orders values('%s','%s','%s','%s','%s','%s','%d')"
                        args = (y,q,w,e,r,t,total)
                        try:
                            print(args)
                            cursor.execute(str%args)
                            conn.commit()
                            tkinter.messagebox.showinfo('Window Title', 'Order Placed')
                        except:
                            conn.rollback()
                        cursor.close()
                        conn.close()
                        r2.destroy()
                        root.destroy()
                    
                    
                    b6=Button(r2,text='Place Order', bg="coral", fg="black", font=("Bookman Old Style",14), bd=0,command=insert).place(x=1100,y=650)
                user()
        except:
            conn.rollback()        
        r2.mainloop()

def exit():
    root.destroy()
signup=Button(root,text='Sign up', bg="coral", fg="black", font=("Arial",14),command=insert_values).place(x=275,y=450)
login=Button(root,text='Login', bg="coral", fg="black", font=("Arial",14),command=validate_admin).place(x=875,y=450)
exit=Button(root,text='Exit', bg="coral", fg="black", font=("Arial",14),command=exit).place(x=1150,y=450)

root.mainloop()


