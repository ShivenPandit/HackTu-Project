from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import sqlite3
import cv2
import numpy as np
from tkinter import messagebox
import face_recognition
import dlib

try:
    # Initialize face detection and alignment tools
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # Check if OpenCV contrib modules are installed
    if not hasattr(cv2, 'face'):
        raise ImportError("OpenCV contrib modules are not installed")
except ImportError:
    # Show error message with installation instructions
    def show_error():
        messagebox.showerror("Module Error", 
            "OpenCV face recognition modules are not installed.\n\n"
            "Please install it using:\n"
            "pip install opencv-contrib-python\n\n"
            "After installation, restart the application.")
        exit(1)

def detect_and_crop_face(image_path, desired_size=(200, 200)):
    """Detect, align and crop face from image"""
    try:
        # Read image
        img = cv2.imread(image_path)
        if img is None:
            return None
            
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = face_detector.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        
        if len(faces) == 0:
            return None
            
        # Get the largest face
        (x, y, w, h) = max(faces, key=lambda f: f[2] * f[3])
        
        # Add margin
        margin = int(0.1 * w)  # 10% margin
        x = max(0, x - margin)
        y = max(0, y - margin)
        w = min(img.shape[1] - x, w + 2 * margin)
        h = min(img.shape[0] - y, h + 2 * margin)
        
        # Crop face
        face = gray[y:y+h, x:x+w]
        
        # Resize to desired size
        face = cv2.resize(face, desired_size, interpolation=cv2.INTER_CUBIC)
        
        # Enhance image
        face = cv2.equalizeHist(face)  # Improve contrast
        
        return face
    except Exception as e:
        print(f"Error processing image {image_path}: {str(e)}")
        return None

class Train:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Train Pannel")

        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"D:\Projects\Facial recognition Attendance\myImages\mybanner.jpg")
        img=img.resize((1366,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"D:\Projects\Facial recognition Attendance\myImages\myt_bg1.jpg")
        bg1=bg1.resize((1366,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Training Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"D:\Projects\Facial recognition Attendance\myImages\myt_btn1.png")
        std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.train_classifier,image=self.std_img1,cursor="hand2")
        std_b1.place(x=600,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.train_classifier,text="Train Dataset",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=600,y=350,width=180,height=45)

    # ==================Create Function of Traing===================
    def train_classifier(self):
        try:
            # Check for required modules
            if not hasattr(cv2, 'face'):
                raise ImportError("OpenCV face recognition modules are not installed")
                
            data_dir = "data"
            
            # Check if directory exists
            if not os.path.exists(data_dir):
                messagebox.showerror("Error", "Data directory not found!", parent=self.root)
                return
                
            # Get all image paths
            path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(('.jpg', '.jpeg', '.png'))]
            
            if len(path) == 0:
                messagebox.showerror("Error", "No images found in data directory!", parent=self.root)
                return
                
            faces = []
            ids = []
            total_images = len(path)
            current_image = 0
            processed_count = 0

            for image in path:
                # Update progress
                current_image += 1
                title_lb1 = Label(self.root, text=f"Processing Images: {current_image}/{total_images}", 
                                font=("verdana", 20, "bold"), bg="white", fg="navyblue")
                title_lb1.place(x=0, y=100, width=1366, height=45)
                self.root.update()

                try:
                    # Detect and crop face
                    face = detect_and_crop_face(image)
                    
                    if face is not None:
                        # Extract ID from filename (student.1.1.jpg -> id = 1)
                        id = int(os.path.split(image)[1].split('.')[1])
                        
                        faces.append(face)
                        ids.append(id)
                        processed_count += 1
                    else:
                        print(f"No face detected in {image}")
                        
                except Exception as e:
                    print(f"Error processing image {image}: {str(e)}")
                    continue

            if len(faces) == 0:
                messagebox.showerror("Error", "No valid faces found in images!", parent=self.root)
                return

            # Train the classifier
            title_lb1 = Label(self.root, text="Training Classifier...", 
                            font=("verdana", 20, "bold"), bg="white", fg="navyblue")
            title_lb1.place(x=0, y=100, width=1366, height=45)
            self.root.update()

            ids = np.array(ids)
            
            # Create and train the LBPH face recognizer with optimized parameters
            clf = cv2.face.LBPHFaceRecognizer_create(
                radius=2,           # Radius of the circular pattern
                neighbors=12,       # Number of sample points
                grid_x=8,          # Number of cells in X direction
                grid_y=8,          # Number of cells in Y direction
                threshold=100.0     # Distance threshold
            )
            clf.train(faces, ids)
            clf.write("clf.xml")

            success_msg = (
                f"Training Completed Successfully!\n"
                f"Total Images Found: {total_images}\n"
                f"Successfully Processed: {processed_count}\n"
                f"Failed/No Face: {total_images - processed_count}"
            )
            messagebox.showinfo("Success", success_msg, parent=self.root)
            
            # Clear progress label
            title_lb1 = Label(self.root, text="Welcome to Training Panel", 
                            font=("verdana", 30, "bold"), bg="white", fg="navyblue")
            title_lb1.place(x=0, y=0, width=1366, height=45)

        except ImportError:
            messagebox.showerror("Module Error", 
                "OpenCV face recognition modules are not installed.\n\n"
                "Please install it using:\n"
                "pip install opencv-contrib-python\n\n"
                "After installation, restart the application.")
        except Exception as e:
            messagebox.showerror("Error", f"Training failed: {str(e)}", parent=self.root)





if __name__ == "__main__":
    root=Tk()
    try:
        if not hasattr(cv2, 'face'):
            show_error()
        obj=Train(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"Application failed to start: {str(e)}")