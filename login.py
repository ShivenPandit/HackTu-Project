from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
from train import Train
from Student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from helpsupport import Helpsupport
import os


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0")

        # variables 
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"D:\Facial recognition Attendance\myImages\myloginBg1.jpg")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame1= Frame(self.root,bg="#002B53")
        frame1.place(x=560,y=170,width=340,height=450)

        img1=Image.open(r"D:\Facial recognition Attendance\myImages\mylog1.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1 = Label(image=self.photoimage1,bg="#002B53")
        lb1img1.place(x=690,y=175, width=100,height=100)

        get_str = Label(frame1,text="Login",font=("times new roman",20,"bold"),fg="white",bg="#002B53")
        get_str.place(x=140,y=100)

        #label1 
        username =lb1= Label(frame1,text="Username:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        username.place(x=30,y=160)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtuser.place(x=33,y=190,width=270)


        #label2 
        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        pwd.place(x=30,y=230)

        #entry2 
        self.txtpwd=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=33,y=260,width=270)


        # Creating Button Login
        loginbtn=Button(frame1,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#002B53",bg="white",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=33,y=320,width=270,height=35)


        # Creating Button Registration
        loginbtn=Button(frame1,command=self.reg,text="Register",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=33,y=370,width=50,height=20)


        # Creating Button Forget
        loginbtn=Button(frame1,command=self.forget_pwd,text="Forget",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=90,y=370,width=50,height=20)


    #  THis function is for open register window
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.txtuser.get()=="admin" and self.txtpwd.get()=="admin"):
            messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System Using Facial Recognition")
        else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            conn = mysql.connector.connect(host="localhost", username="root", password="Shiven@12", database="Login")
            mycursor = conn.cursor()
            mycursor.execute("select * from register where email=%s and pwd=%s",(
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                open_min=messagebox.askyesno("YesNo","Access only Admin")
                if open_min>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_system(self.new_window)
                else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()
#=======================Reset Passowrd Function=============================
    def reset_pass(self):
        if self.var_ssq.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Shiven@12", database="Login")
            mycursor = conn.cursor()
            query=("select * from register where email=%s and ss_que=%s and s_ans=%s")
            value=(self.txtuser.get(),self.var_ssq.get(),self.var_sa.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
            else:
                query=("update register set pwd=%s where email=%s")
                value=(self.var_pwd.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been rest, Please login with new Password!",parent=self.root2)
                



# =====================Forget window=========================================
    def forget_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email ID to reset Password!")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Shiven@12", database="Login")
            mycursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x400+610+170")
                l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                l.place(x=0,y=10,relwidth=1)
                # -------------------fields-------------------
                #label1 
                ssq =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                ssq.place(x=70,y=80)

                #Combo Box1
                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)


                #label2 
                sa =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                sa.place(x=70,y=150)

                #entry2 
                self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_sa,font=("times new roman",15,"bold"))
                self.txtpwd.place(x=70,y=180,width=270)

                #label2 
                new_pwd =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                new_pwd.place(x=70,y=220)

                #entry2 
                self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
                self.new_pwd.place(x=70,y=250,width=270)

                # Creating Button New Password
                loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=70,y=300,width=270,height=35)


            

# =====================main program Face deteion system====================

class Face_Recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
    # first image
        img=Image.open(r"D:\Facial recognition Attendance\myImages\myfg.jpg")
        img = img.resize((520, 130), Image.LANCZOS) # the resize 
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=520,height=130)
        
    # second image
        img1=Image.open(r"D:\Facial recognition Attendance\myImages\mytech.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS) # the resize 
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=520,y=0,width=500,height=130)
        
    # third image
        img2=Image.open(r"D:\Facial recognition Attendance\myImages\mytech1.jpg")
        img2 = img2.resize((520, 130), Image.LANCZOS) # the resize 
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1020,y=0,width=520,height=130)    
        
        
    # bg image
        img3=Image.open(r"D:\Facial recognition Attendance\myImages\mybg2.jpg")
        img3 = img3.resize((1540, 790), Image.LANCZOS) # the resize 
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1540,height=790)
        
    # For title lbl
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45) 
        
    # student button
        img4=Image.open(r"D:\Facial recognition Attendance\myImages\mydata1.jpg")
        img4 = img4.resize((220, 220), Image.LANCZOS) # the resize 
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)
        
    # Detect button
        img5=Image.open(r"D:\Facial recognition Attendance\myImages\mydetect.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS) # the resize 
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,command=self.face_recognition,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Face Detector",command=self.face_recognition,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)
        
    # Attendance button
        img6=Image.open(r"D:\Facial recognition Attendance\myImages\myattend1.png")
        img6 = img6.resize((220, 220), Image.LANCZOS) # the resize 
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)
        
        b1_2=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_2.place(x=800,y=300,width=220,height=40)
            
    # Help Desk button
        img7=Image.open(r"D:\Facial recognition Attendance\myImages\myhelp.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS) # the resize 
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,command=self.help_support,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1_3=Button(bg_img,text="Help Desk",command=self.help_support,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_3.place(x=1100,y=300,width=220,height=40)
        
        
    # Train Data button
        img8=Image.open(r"D:\Facial recognition Attendance\myImages\mytrain.jpg")
        img8 = img8.resize((220, 220), Image.LANCZOS) # the resize 
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,command=self.train,cursor="hand2")
        b1.place(x=200,y=400,width=220,height=220)
        
        b1_4=Button(bg_img,text="Train Data",cursor="hand2",command=self.train,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_4.place(x=200,y=600,width=220,height=40)
        
        
    # Photos button
        img9=Image.open(r"D:\Facial recognition Attendance\myImages\myphoto.jpg")
        img9 = img9.resize((220, 220), Image.LANCZOS) # the resize 
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,command=self.open_img,cursor="hand2")
        b1.place(x=500,y=400,width=220,height=220)
        
        b1_5=Button(bg_img,text="Photos",command=self.open_img,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_5.place(x=500,y=600,width=220,height=40)
        
        
    # Developer button
        img10=Image.open(r"D:\Facial recognition Attendance\myImages\mydev.jpg")
        img10 = img10.resize((220, 220), Image.LANCZOS) # the resize 
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,command=self.developer,cursor="hand2")
        b1.place(x=800,y=400,width=220,height=220)
        
        b1_6=Button(bg_img,text="Developer",command=self.developer,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_6.place(x=800,y=600,width=220,height=40)
        
        
    # Exit button
        img11=Image.open(r"D:\Facial recognition Attendance\myImages\myexit.jpg")
        img11 = img11.resize((220, 220), Image.LANCZOS) # the resize 
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,command=self.Close,cursor="hand2")
        b1.place(x=1100,y=400,width=220,height=220)
        
        b1_7=Button(bg_img,text="Exit",command=self.Close,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_7.place(x=1100,y=600,width=220,height=40)
      
    
    def open_img(self):
        os.startfile("data")
    # ================ Function Buttons ===================
    
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def help_support(self):
        self.new_window1=Toplevel(self.root)
        self.app=Helpsupport(self.new_window1)
        
    def face_recognition(self):
        self.new_window1=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window1)
        
    def train(self):
        self.new_window1=Toplevel(self.root)
        self.app=Train(self.new_window1)
        
    def developer(self):
        self.new_window1=Toplevel(self.root)
        self.app=Developer(self.new_window1)
    
    def Close(self):
        root.destroy()
        
        



if __name__ == "__main__":
    root=Tk()
    app=Login(root)
    root.mainloop()