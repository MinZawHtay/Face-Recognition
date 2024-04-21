import cv2
image = cv2.imread('VIJAY.jpg')
cap = cv2.VideoCapture(0)  # 0 represents the default camera (usually the built-in webcam)
face_cascade = cv2.CascadeClassifier('haar_face.xml')
# Convert the image to grayscale (required for the face detection algorithm)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the grayscale image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('Face Detection', image)
cv2.waitKey(0)  # This will display the image until a key is pressed
cv2.destroyAllWindows()  # Close all OpenCV windows
cap.release()
