import cv2
import numpy as np
import mysql.connector
from datetime import datetime
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class FaceRecognition:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Panel")

        self.setup_gui()

    def setup_gui(self):
        # Header image
        img = Image.open(r"D:\Facial recognition Attendance\myImages\mybanner.jpg")
        img = img.resize((1366, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        header_label = Label(self.root, image=self.photoimg)
        header_label.place(x=0, y=0, width=1366, height=130)

        # Background image
        bg_img = Image.open(r"D:\Facial recognition Attendance\myImages\mybg2.jpg")
        bg_img = bg_img.resize((1366, 768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg_img)
        bg_label = Label(self.root, image=self.photobg1)
        bg_label.place(x=0, y=130, width=1366, height=768)

        # Title section
        title_label = Label(bg_label, text="Welcome to Face Recognition Panel", font=("verdana", 30, "bold"),
                            bg="white", fg="navyblue")
        title_label.place(x=0, y=0, width=1366, height=45)

        # Create buttons below the section
        std_img_btn = Image.open(r"D:\Facial recognition Attendance\myImages\myf_det.jpg")
        std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_button = Button(bg_label, command=self.face_recognition, image=self.std_img1, cursor="hand2")
        std_button.place(x=600, y=170, width=180, height=180)

        std_button_label = Button(bg_label, command=self.face_recognition, text="Face Detector", cursor="hand2",
                                  font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        std_button_label.place(x=600, y=350, width=180, height=45)

    def mark_attendance(self, student_id, roll_no, student_name):
        with open("attendance.csv", "r+", newline="\n") as f:
            my_data_list = f.readlines()
            name_list = []

            for line in my_data_list:
                entry = line.split(",")
                name_list.append(entry[0])

            if (student_id not in name_list) and (roll_no not in name_list) and (student_name not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dt_string = now.strftime("%H:%M:%S")
                f.writelines(f"\n{student_id}, {roll_no}, {student_name}, {dt_string}, {d1}, Present")

    def face_recognition(self):
        def draw_boundary(img, classifier, scale_factor, min_neighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scale_factor, min_neighbors)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])

                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Shiven@12",
                                               database="facial_recognition_attendance")
                my_cursor = conn.cursor()

                my_cursor.execute(f"select Name from student where Student_id={id}")
                student_name = my_cursor.fetchone()
                student_name = student_name[0] if student_name else "Shiven"

                my_cursor.execute(f"select Roll from student where Student_id={id}")
                roll_no = my_cursor.fetchone()
                roll_no = roll_no[0] if roll_no else "2232168"

                if confidence > 77:
                    cv2.putText(img, f"Student_ID: {id}", (x, y - 60), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Name: {student_name}", (x, y - 40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Roll-No: {roll_no}", (x, y - 20), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    self.mark_attendance(id, roll_no, student_name)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

            return img

        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face_LBPHFaceRecognizer.create()
        clf.read("clf.xml")

        video_capture = cv2.VideoCapture(0)

        while True:
            ret, img = video_capture.read()
            img = draw_boundary(img, face_cascade, 1.1, 10, (0, 255, 0), "Face", clf)
            cv2.imshow("Face Detector", img)

            if cv2.waitKey(1) == 13:
                break

        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    app = FaceRecognition(root)
    root.mainloop()
