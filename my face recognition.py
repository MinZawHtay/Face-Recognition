import dlib
import cv2
import face_recognition
import os
import pyttsx3
from time import sleep
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# Create a directory to save the recognized faces
output_directory = 'recognized_faces'
os.makedirs(output_directory, exist_ok=True)

known_face_encodings = []
known_face_names = []

# Load and encode known faces (including the new person)
for filename, name in [
    (r'D:\Python project\Face Detection\321654.png', 'Sathiyar'),
    (r'D:\Python project\Face Detection\navi.jpg', 'Navi'),
    (r'D:\Python project\Face Detection\VIJAY.jpg', 'Vijay'),
    (r'D:\Python project\Face Detection\963852.png', 'Elon musk'),
    ]:
    image = face_recognition.load_image_file(filename)
    encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(encoding)
    known_face_names.append(name)

image = cv2.imread('VIJAY.jpg')
cap = cv2.VideoCapture(0)  # 0 represents the default camera (usually the built-in webcam)

# ...

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Find all face locations and encodings in the frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for i, (top, right, bottom, left) in enumerate(face_locations):
        # Compare the face encoding to known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encodings[i])

        name = "Unknown"
        confidence = 0  # Initialize confidence to 0

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index].upper()  # Convert name to uppercase

            # Calculate the face distance (lower value indicates a better match)
            face_distances = face_recognition.face_distance(known_face_encodings, face_encodings[i])
            confidence = 100 - (face_distances[first_match_index] * 100)

        # Draw a rectangle and label on the image with green background and bold green text
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.rectangle(frame, (left, top - 20), (right, top), (0, 255, 0), cv2.FILLED)  # Green background
        text = f"{name} ({confidence:.2f}%)"
        cv2.putText(frame, text, (left + 6, top - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)  # Bold green text

        # Check if the recognized face is "Sathiyar" and confidence is 50% or more
        if name == "SATHIYAR" and confidence >= 50:
            speak(f"Hi,  {name}  Sir, your  face  recognition  has  done!")
            sleep(2)
            # Run the Jarvis project (subprocess command or function call)
            # Replace with your Jarvis script

            # Exit the program
            cap.release()
            cv2.destroyAllWindows()
            exit()

        # Save the frame containing the recognized face with the person's name
        if name != "Unknown":
            save_path = os.path.join(output_directory, f"{name}_{i}.jpg")
            cv2.imwrite(save_path, frame)

    # Display the frame with recognized faces
    cv2.imshow('Face Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
