import cv2
import face_recognition

# Load a sample image of your face for comparison
known_face_image = face_recognition.load_image_file("1694693582010.jpg")
known_face_encoding = face_recognition.face_encodings(known_face_image)[0]

# Create a capture object for the webcam (0 is typically the built-in webcam)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Find face locations in the current frame
    face_locations = face_recognition.face_locations(frame)

    if len(face_locations) > 0:
        # Encode the found face
        face_encoding = face_recognition.face_encodings(frame, face_locations)[0]

        # Compare the found face with the known face
        results = face_recognition.compare_faces([known_face_encoding], face_encoding)

        if results[0]:
            print("Face recognized. Unlocking the PC.")
            # Implement a method to unlock the PC here
            # You might need to use third-party libraries or system commands to unlock the PC.
            # For example, you can use pyautogui to simulate keyboard shortcuts to unlock the PC.
            # Be cautious with this part, as unlocking a PC securely is a complex task.

    # Display the webcam feed
    cv2.imshow('Face Lock', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
