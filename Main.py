from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # use for images
from Student import Student
from helpsupport import Helpsupport
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from train import Train
import os


class Face_Recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # first image
        img = Image.open(r"D:\Facial recognition Attendance\myImages\myfg.jpg")
        img = img.resize((520, 130), Image.LANCZOS)  # the resize
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=520, height=130)

        # second image
        img1 = Image.open(r"D:\Facial recognition Attendance\myImages\mytech.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)  # the resize
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=520, y=0, width=500, height=130)

        # third image
        img2 = Image.open(r"D:\Facial recognition Attendance\myImages\mytech1.jpg")
        img2 = img2.resize((520, 130), Image.LANCZOS)  # the resize
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1020, y=0, width=520, height=130)

        # bg image
        img3 = Image.open(r"D:\Facial recognition Attendance\myImages\mybg2.jpg")
        img3 = img3.resize((1540, 790), Image.LANCZOS)  # the resize
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1540, height=790)

        # For title lbl
        title_lbl = Label(
            bg_img,
            text="FACE RECOGNITION ATTENDANCE SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="red",
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # student button
        img4 = Image.open(r"D:\Facial recognition Attendance\myImages\mydata1.jpg")
        img4 = img4.resize((220, 220), Image.LANCZOS)  # the resize
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(
            bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2"
        )
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(
            bg_img,
            text="Student Details",
            command=self.student_details,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=200, y=300, width=220, height=40)

        # Detect button
        img5 = Image.open(r"D:\Facial recognition Attendance\myImages\mydetect.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)  # the resize
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(
            bg_img, image=self.photoimg5, command=self.face_recognition, cursor="hand2"
        )
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(
            bg_img,
            text="Face Detector",
            command=self.face_recognition,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=500, y=300, width=220, height=40)

        # Attendance button
        img6 = Image.open(r"D:\Facial recognition Attendance\myImages\myattend1.png")
        img6 = img6.resize((220, 220), Image.LANCZOS)  # the resize
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(
            bg_img, image=self.photoimg6, command=self.attendence, cursor="hand2"
        )
        b1.place(x=800, y=100, width=220, height=220)

        b1_2 = Button(
            bg_img,
            text="Attendance",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_2.place(x=800, y=300, width=220, height=40)

        # Help Desk button
        img7 = Image.open(r"D:\Facial recognition Attendance\myImages\myhelp.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS)  # the resize
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(
            bg_img, image=self.photoimg7, command=self.help_support, cursor="hand2"
        )
        b1.place(x=1100, y=100, width=220, height=220)

        b1_3 = Button(
            bg_img,
            text="Help Desk",
            command=self.help_support,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_3.place(x=1100, y=300, width=220, height=40)

        # Train Data button
        img8 = Image.open(r"D:\Facial recognition Attendance\myImages\mytrain.jpg")
        img8 = img8.resize((220, 220), Image.LANCZOS)  # the resize
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, command=self.train, cursor="hand2")
        b1.place(x=200, y=400, width=220, height=220)

        b1_4 = Button(
            bg_img,
            text="Train Data",
            cursor="hand2",
            command=self.train,
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_4.place(x=200, y=600, width=220, height=40)

        # Photos button
        img9 = Image.open(r"D:\Facial recognition Attendance\myImages\myphoto.jpg")
        img9 = img9.resize((220, 220), Image.LANCZOS)  # the resize
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, command=self.open_img, cursor="hand2")
        b1.place(x=500, y=400, width=220, height=220)

        b1_5 = Button(
            bg_img,
            text="Photos",
            command=self.open_img,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_5.place(x=500, y=600, width=220, height=40)

        # Developer button
        img10 = Image.open(r"D:\Facial recognition Attendance\myImages\mydev.jpg")
        img10 = img10.resize((220, 220), Image.LANCZOS)  # the resize
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(
            bg_img, image=self.photoimg10, command=self.developer, cursor="hand2"
        )
        b1.place(x=800, y=400, width=220, height=220)

        b1_6 = Button(
            bg_img,
            text="Developer",
            command=self.developer,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_6.place(x=800, y=600, width=220, height=40)

        # Exit button
        img11 = Image.open(r"D:\Facial recognition Attendance\myImages\myexit.jpg")
        img11 = img11.resize((220, 220), Image.LANCZOS)  # the resize
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, command=self.Close, cursor="hand2")
        b1.place(x=1100, y=400, width=220, height=220)

        b1_7 = Button(
            bg_img,
            text="Exit",
            command=self.Close,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_7.place(x=1100, y=600, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    # ================ Function Buttons ===================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def help_support(self):
        self.new_window1 = Toplevel(self.root)
        self.app = Helpsupport(self.new_window1)

    def face_recognition(self):
        self.new_window1 = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window1)

    def train(self):
        self.new_window1 = Toplevel(self.root)
        self.app = Train(self.new_window1)

    def developer(self):
        self.new_window1 = Toplevel(self.root)
        self.app = Developer(self.new_window1)

    def attendence(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def Close(self):
        root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_system(root)
    root.mainloop()
