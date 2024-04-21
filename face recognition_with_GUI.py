import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import dlib
import cv2
import face_recognition
import os

# Create a directory to save the recognized faces
output_directory = 'recognized_faces'
os.makedirs(output_directory, exist_ok=True)

# Function to recognize and save faces
def recognize_and_save_faces():
    if name != "Unknown":
            save_path = os.path.join(output_directory, f"{name}_{i}.jpg")
            cv2.imwrite(save_path, frame)

    # Your face recognition code here (same as the code you provided)
    # ...

# Function to select an image for recognition
def browse_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image_path.set(file_path)

# Create the main window
root = tk.Tk()
root.title("Face Recognition App")

# Create a frame for widgets
frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Label and Entry for image path
ttk.Label(frame, text="Select Image:").grid(row=0, column=0, sticky=tk.W)
image_path = tk.StringVar()
entry_image_path = ttk.Entry(frame, textvariable=image_path)
entry_image_path.grid(row=0, column=1, sticky=(tk.W, tk.E))
ttk.Button(frame, text="Browse", command=browse_image).grid(row=0, column=2, sticky=tk.W)

# Button to recognize and save faces
ttk.Button(frame, text="Recognize and Save Faces", command=recognize_and_save_faces).grid(row=1, column=0, columnspan=3)

# Start the GUI main loop
root.mainloop()
