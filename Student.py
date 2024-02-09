from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # use for images
from tkinter import messagebox
import mysql.connector
import os
import cv2
import time


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student")

        # ======== Variables ==========
        self.var_depart = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_photo = StringVar()

        # first image
        img = Image.open(r"D:\Facial recognition Attendance\myImages\mystu.jpg")
        img = img.resize((520, 130), Image.LANCZOS)  # the resize
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=520, height=130)

        # second image
        img1 = Image.open(r"D:\Facial recognition Attendance\myImages\mysatt.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)  # the resize
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=520, y=0, width=500, height=130)

        # third image
        img2 = Image.open(r"D:\Facial recognition Attendance\myImages\mystud.jpg")
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
            text="STUDENT MANAGEMENT SYSTEM ",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="Dark Green",
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1500, height=600)

        # left label frame
        Left_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Student Details",
            font=("times new roman", 16, "bold"),
        )
        Left_frame.place(x=10, y=2, width=730, height=593)

        # left lablel image
        img_left = Image.open(
            r"D:\Facial recognition Attendance\myImages\mysdetail.jpg"
        )
        img_left = img_left.resize((720, 130), Image.LANCZOS)  # the resize
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        # Current course information
        Current_Course_frame = LabelFrame(
            Left_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Current Course Information",
            font=("times new roman", 16, "bold"),
        )
        Current_Course_frame.place(x=5, y=130, width=715, height=130)

        # Department
        dep_label = Label(
            Current_Course_frame,
            text="Department",
            font=("times new roman", 16, "bold"),
            bg="white",
        )
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(
            Current_Course_frame,
            textvariable=self.var_depart,
            font=("times new roman", 16, "bold"),
            width=17,
            state="readonly",
        )
        dep_combo["values"] = ("Select Department", "CSE", "IT", "Civil", "Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        dep_label = Label(
            Current_Course_frame,
            text="Course",
            font=("times new roman", 16, "bold"),
            bg="white",
        )
        dep_label.grid(row=0, column=2, padx=10, sticky=W)

        dep_combo = ttk.Combobox(
            Current_Course_frame,
            textvariable=self.var_course,
            font=("times new roman", 16, "bold"),
            width=17,
            state="readonly",
        )
        dep_combo["values"] = ("Select Course", "Btech", "diploma", "MBA", "BSE")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        dep_label = Label(
            Current_Course_frame,
            text="Year",
            font=("times new roman", 16, "bold"),
            bg="white",
        )
        dep_label.grid(row=1, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(
            Current_Course_frame,
            textvariable=self.var_year,
            font=("times new roman", 16, "bold"),
            width=17,
            state="readonly",
        )
        dep_combo["values"] = (
            "Select Year",
            "2019-20",
            "2020-21",
            "2021-22",
            "2022-23",
            "2023-24",
            "2024-25",
        )
        dep_combo.current(0)
        dep_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        dep_label = Label(
            Current_Course_frame,
            text="Semester",
            font=("times new roman", 16, "bold"),
            bg="white",
        )
        dep_label.grid(row=1, column=2, padx=10, sticky=W)

        dep_combo = ttk.Combobox(
            Current_Course_frame,
            textvariable=self.var_semester,
            font=("times new roman", 16, "bold"),
            width=17,
            state="readonly",
        )
        dep_combo["values"] = (
            "Select Semester",
            "Semester-1",
            "Semester-2",
            "Semester-3",
            "Semester-4",
            "Semester-5",
            "Semester-6",
            "Semester-7",
            "Semester-8",
        )
        dep_combo.current(0)
        dep_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student information
        Class_student_frame = LabelFrame(
            Left_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Current Student Information",
            font=("times new roman", 16, "bold"),
        )
        Class_student_frame.place(x=5, y=250, width=715, height=330)

        # Student ID
        StudentID_frame = Label(
            Class_student_frame,
            text="Student ID",
            font=("times new roman", 14, "bold"),
            bg="white",
        )
        StudentID_frame.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        StudentID_entry = ttk.Entry(
            Class_student_frame,
            textvariable=self.var_std_id,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        StudentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        StudentID_frame = Label(
            Class_student_frame,
            text="Student Name",
            font=("times new roman", 14, "bold"),
            bg="white",
        )
        StudentID_frame.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        StudentID_entry = ttk.Entry(
            Class_student_frame,
            textvariable=self.var_std_name,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        StudentID_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division
        StudentID_frame = Label(
            Class_student_frame,
            text="Class Division",
            font=("times new roman", 14, "bold"),
            bg="white",
        )
        StudentID_frame.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        # StudentID_entry=ttk.Entry(Class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",13,"bold"))
        # StudentID_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        division_combo = ttk.Combobox(
            Class_student_frame,
            textvariable=self.var_div,
            font=("times new roman", 13, "bold"),
            width=18,
            state="readonly",
        )
        division_combo["values"] = ("A", "B", "C")
        division_combo.current(0)
        division_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll Number
        StudentID_frame = Label(
            Class_student_frame,
            text="Roll Number",
            font=("times new roman", 14, "bold"),
            bg="white",
        )
        StudentID_frame.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        StudentID_entry = ttk.Entry(
            Class_student_frame,
            textvariable=self.var_roll,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        StudentID_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        StudentID_frame = Label(
            Class_student_frame,
            text="Gender",
            font=("times new roman", 14, "bold"),
            bg="white",
        )
        StudentID_frame.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        # StudentID_entry=ttk.Entry(Class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        # StudentID_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        gender_combo = ttk.Combobox(
            Class_student_frame,
            textvariable=self.var_gender,
            font=("times new roman", 13, "bold"),
            width=18,
            state="readonly",
        )
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB
        StudentID_frame = Label(
            Class_student_frame,
            text="DOB",
            font=("times new roman", 14, "bold"),
            bg="white",
        )
        StudentID_frame.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        StudentID_entry = ttk.Entry(
            Class_student_frame,
            textvariable=self.var_dob,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        StudentID_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        StudentID_frame = Label(
            Class_student_frame,
            text="Email",
            font=("times new roman", 14, "bold"),
            bg="white",
        )
        StudentID_frame.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        StudentID_entry = ttk.Entry(
            Class_student_frame,
            textvariable=self.var_email,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        StudentID_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone Number
        StudentID_frame = Label(
            Class_student_frame,
            text="Phone Number",
            font=("times new roman", 14, "bold"),
            bg="white",
        )
        StudentID_frame.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        StudentID_entry = ttk.Entry(
            Class_student_frame,
            textvariable=self.var_phone,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        StudentID_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        StudentID_frame = Label(
            Class_student_frame,
            text="Address",
            font=("times new roman", 14, "bold"),
            bg="white",
        )
        StudentID_frame.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        StudentID_entry = ttk.Entry(
            Class_student_frame,
            textvariable=self.var_address,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        StudentID_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name
        StudentID_frame = Label(
            Class_student_frame,
            text="Teacher Name",
            font=("times new roman", 14, "bold"),
            bg="white",
        )
        StudentID_frame.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        StudentID_entry = ttk.Entry(
            Class_student_frame,
            textvariable=self.var_teacher,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        StudentID_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Radio Buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            Class_student_frame,
            variable=self.var_radio1,
            text="Take Photo Sample",
            value="Yes",
        )
        radiobtn1.grid(row=5, column=0)

        radiobtn2 = ttk.Radiobutton(
            Class_student_frame,
            variable=self.var_radio1,
            text="No Photo Sample",
            value="No",
        )
        radiobtn2.grid(row=5, column=1)

        # Buttons Frame
        btn_frame = Frame(Class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=215, width=700, height=80)
        # uper buttons
        save_btn = Button(
            btn_frame,
            text="Save",
            command=self.add_data,
            width=17,
            height=1,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        save_btn.grid(row=0, column=0)

        update_btn = Button(
            btn_frame,
            text="Update",
            command=self.update_data,
            width=16,
            height=1,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        update_btn.grid(row=0, column=1)

        delete_btn = Button(
            btn_frame,
            text="Delete",
            command=self.delete_data,
            width=16,
            height=1,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(
            btn_frame,
            text="Reset",
            command=self.reset_data,
            width=17,
            height=1,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        reset_btn.grid(row=0, column=3)
        # lower buttons frame
        btn1_frame = Frame(Class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn1_frame.place(x=5, y=250, width=700, height=50)

        take_photo_btn = Button(
            btn1_frame,
            text="Take Photo Sample",
            command=self.generate_dataset,
            width=23,
            height=1,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        take_photo_btn.grid(row=1, column=0)

        update_photo_btn = Button(
            btn1_frame,
            text="Update Photo Sample",
            width=22,
            height=1,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )

        # right label frame
        Right_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Student Details",
            font=("times new roman", 16, "bold"),
        )
        Right_frame.place(x=750, y=2, width=730, height=593)

        # Right lablel image
        img_Right = Image.open(
            r"D:\Facial recognition Attendance\myImages\mystudent.jpg"
        )
        img_Right = img_Right.resize((720, 130), Image.LANCZOS)  # the resize
        self.photoimg_Right = ImageTk.PhotoImage(img_Right)

        f_lbl = Label(Right_frame, image=self.photoimg_Right)
        f_lbl.place(x=5, y=0, width=720, height=130)

        # ====== Search System =========
        Search_frame = LabelFrame(
            Right_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Search System",
            font=("times new roman", 16, "bold"),
        )
        Search_frame.place(x=3, y=130, width=718, height=70)

        Search_Lable = Label(
            Search_frame,
            text="Search by:",
            font=("times new roman", 15, "bold"),
            bg="red",
            fg="white",
        )
        Search_Lable.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        Search_combo = ttk.Combobox(
            Search_frame,
            font=("times new roman", 13, "bold"),
            width=15,
            state="readonly",
        )
        Search_combo["values"] = ("Select", "Roll number", "Name", "Phone Number")
        Search_combo.current(0)
        Search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        Search_entry = ttk.Entry(
            Search_frame, width=20, font=("times new roman", 13, "bold")
        )
        Search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        Search_btn = Button(
            Search_frame,
            text="Search",
            width=10,
            height=1,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        Search_btn.grid(row=0, column=3)

        ShowAll_btn = Button(
            Search_frame,
            text="Show All",
            width=10,
            height=1,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        ShowAll_btn.grid(row=0, column=4)

        # ======= Table Frame =======
        Table_frame = LabelFrame(
            Right_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="",
            font=("times new roman", 16, "bold"),
        )
        Table_frame.place(x=3, y=204, width=718, height=360)

        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            Table_frame,
            columns=(
                "depart",
                "course",
                "year",
                "sem",
                "id",
                "name",
                "div",
                "roll",
                "dob",
                "email",
                "gender",
                "phone",
                "address",
                "teacher",
                "photo",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("depart", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo")
        self.student_table["show"] = "headings"

        self.student_table.column("depart", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ================== Function Decration =================

    def add_data(self):
        if (
            self.var_depart.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.var_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Shiven@12",
                    database="facial_recognition_attendance",
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_depart.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                    ),
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success",
                    "Student details has been added Sucessfully",
                    parent=self.root,
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # ================= Fetch data ====================
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Shiven@12",
            database="facial_recognition_attendance",
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
            conn.close()

    # ================== Get Curser ======================
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_depart.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # ===== update function =====
    def update_data(self):
        if (
            self.var_depart.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.var_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno(
                    "Update",
                    "Do you want to update this student's details",
                    parent=self.root,
                )
                if update > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="Shiven@12",
                        database="facial_recognition_attendance",
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "UPDATE student SET Depart=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s WHERE Student_id=%s",
                        (
                            self.var_depart.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get(),
                        ),
                    )
                    messagebox.showinfo(
                        "Success",
                        "Student details successfully updated",
                        parent=self.root,
                    )
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # ===== delete function =======
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "Student id must be required", parent=self.root
            )
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Page",
                    "Do you want to delete this student",
                    parent=self.root,
                )
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="Shiven@12",
                        database="facial_recognition_attendance",
                    )
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM student WHERE Student_id=%s"  # Specify the table name 'student' after DELETE
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo(
                        "Delete",
                        "Successfully deleted student details",
                        parent=self.root,
                    )
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # ===== reset function =======
    def reset_data(self):
        self.var_depart.set("Select Department")
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("A"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

    # ================ Generate data set or Take photo Sample ======================
    def generate_dataset(self):
        if (
            self.var_depart.get() == "Select Department"
            or self.var_std_name.get() == ""
        ):
            messagebox.showerror(
                "Error", "Department and Name fields are required", parent=self.root
            )
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Shiven@12",
                    database="facial_recognition_attendance",
                )
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myreslut = my_cursor.fetchall()
                id = 0
                for x in myreslut:
                    id += 1

                my_cursor.execute(
                    "UPDATE student SET Depart=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s WHERE Student_id=%s",
                    (
                        self.var_depart.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        id,
                    ),
                )
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Haar cascade algorithm
                # Load predefined data on face frontals from OpenCV
                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml"
                )

                # Function to crop faces
                def face_cropped(img):
                    # convert grayscale
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # Scaling factor 1.3
                    # Minimum neighbors 5
                    for x, y, w, h in faces:
                        face_cropped = img[y : y + h, x : x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (200, 200))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                        # Generate a unique file name using a timestamp
                        timestamp = int(time.time())  # Get current timestamp
                        file_path = f"data/student.{id}.{img_id}.{timestamp}.jpg"
                        cv2.imwrite(file_path, face)
                        cv2.putText(
                            face,
                            str(img_id),
                            (50, 50),
                            cv2.FONT_HERSHEY_COMPLEX,
                            2,
                            (0, 255, 0),
                            2,
                        )
                        cv2.imshow("Capture Images", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo(
                    "Result", "Generating dataset completed!", parent=self.root
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
