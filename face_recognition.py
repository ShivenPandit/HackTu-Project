import re
import face_recognition
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import sqlite3
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime

class Face_Recognition:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Panel")

        # Initialize video capture as None
        self.cap = None
        
        # Load the face cascade classifier
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        # Load the trained classifier
        self.clf = cv2.face.LBPHFaceRecognizer_create()
        try:
            self.clf.read("clf.xml")
        except Exception as e:
            messagebox.showerror("Error", "Classifier file not found! Please train the system first.")
            return

        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"D:\Projects\Facial recognition Attendance\myImages\mybanner.jpg")
        img=img.resize((1366,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"D:\Projects\Facial recognition Attendance\myImages\mybg2.jpg")
        bg1=bg1.resize((1366,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Face Recognition Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"D:\Projects\Facial recognition Attendance\myImages\myf_det.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.face_recog,image=self.std_img1,cursor="hand2")
        std_b1.place(x=600,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=600,y=350,width=180,height=45)
        
    #=====================Attendance===================
    def mark_attendance(self,i,r,n):
        try:
            current_time = datetime.now()
            d1 = current_time.strftime("%d/%m/%Y")
            dtString = current_time.strftime("%H:%M:%S")
            
            # Check if student already marked attendance today
            with open("attendance.csv", "r+") as f:
                myDatalist = f.readlines()
                name_list = []
                for line in myDatalist:
                    entry = line.split(",")
                    # Check if entry has enough elements and contains today's date
                    if len(entry) >= 5 and entry[4].strip() == d1:
                        name_list.append(entry[0].strip())
                
                if i not in name_list:
                    f.writelines(f"\\n{i}, {r}, {n}, {dtString}, {d1}, Present")
                    return True
            return False
        except Exception as e:
            print(f"Error marking attendance: {str(e)}")
            return False

    def get_student_details(self, student_id):
        try:
            conn = sqlite3.connect("face_recognizer.db")
            cursor = conn.cursor()
            
            # Get all required details in one query
            cursor.execute("""
                SELECT Name, Roll, Student_id 
                FROM student 
                WHERE Student_id=?
            """, (student_id,))
            
            result = cursor.fetchone()
            conn.close()
            
            if result:
                return {"name": result[0], "roll": result[1], "id": result[2]}
            return None
        except Exception as e:
            print(f"Database error: {str(e)}")
            return None

    #================face recognition==================
    def face_recog(self):
        def draw_boundary(img, student_info, x, y, w, h, confidence):
            # Draw rectangle around face
            if confidence > 77:
                color = (0, 255, 0)  # Green for recognized
                # Draw filled rectangle for text background
                cv2.rectangle(img, (x, y-90), (x+w, y), (255, 255, 255), -1)
                # Draw face rectangle
                cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
                # Put text
                cv2.putText(img, f"ID: {student_info['id']}", (x+5, y-60), cv2.FONT_HERSHEY_COMPLEX, 0.8, (51, 51, 153), 2)
                cv2.putText(img, f"Name: {student_info['name']}", (x+5, y-35), cv2.FONT_HERSHEY_COMPLEX, 0.8, (51, 51, 153), 2)
                cv2.putText(img, f"Roll: {student_info['roll']}", (x+5, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (51, 51, 153), 2)
            else:
                color = (0, 0, 255)  # Red for unrecognized
                cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
                cv2.putText(img, "Unknown", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 2)

        try:
            # Initialize video capture
            if self.cap is None:
                self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Try DirectShow
                if not self.cap.isOpened():
                    self.cap = cv2.VideoCapture(0)  # Fallback to default
                
                if not self.cap.isOpened():
                    messagebox.showerror("Error", "Could not open camera!")
                    return
                
                # Set camera properties for better quality
                self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
                self.cap.set(cv2.CAP_PROP_FPS, 30)

            while True:
                ret, frame = self.cap.read()
                if not ret:
                    messagebox.showerror("Error", "Failed to grab frame from camera!")
                    break

                # Convert to grayscale
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                
                # Detect faces
                faces = self.face_cascade.detectMultiScale(
                    gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30),
                    flags=cv2.CASCADE_SCALE_IMAGE
                )

                for (x, y, w, h) in faces:
                    face_roi = gray[y:y+h, x:x+w]
                    
                    # Predict the face
                    try:
                        id, confidence = self.clf.predict(face_roi)
                        confidence = 100 - int(confidence)
                        
                        if confidence > 50:  # Threshold for recognition
                            student_info = self.get_student_details(str(id))
                            if student_info:
                                # Draw boundary and show info
                                draw_boundary(frame, student_info, x, y, w, h, confidence)
                                
                                # Mark attendance
                                if confidence > 77:
                                    if self.mark_attendance(student_info['id'], student_info['roll'], student_info['name']):
                                        # Show small confirmation text
                                        cv2.putText(frame, "Attendance Marked!", (10, 30), 
                                                  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                        else:
                            draw_boundary(frame, None, x, y, w, h, 0)
                    except Exception as e:
                        print(f"Error in prediction: {str(e)}")
                        continue

                cv2.imshow("Face Recognition", frame)

                # Break loop on 'q' press or window close
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                
                # Check if window was closed
                if cv2.getWindowProperty('Face Recognition', cv2.WND_PROP_VISIBLE) < 1:
                    break

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            # Clean up
            if self.cap is not None:
                self.cap.release()
                self.cap = None
            cv2.destroyAllWindows()




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()