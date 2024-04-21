import dlib
import cv2
import face_recognition
known_face_encodings = []
known_face_names = []

for filename, name in [('1694693582010.jpg', 'Sathiyar'), ('navi.jpg', 'Navi'), ('Thalapathy.jpg', 'Vijay')]:
    image = face_recognition.load_image_file(filename)
    encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(encoding)
    known_face_names.append(name)
image_to_recognize = cv2.imread('sathiya.jpg')
face_locations = face_recognition.face_locations(image_to_recognize)
face_encodings = face_recognition.face_encodings(image_to_recognize, face_locations)

for face_encoding in face_encodings:
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Unknown"
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]
    print(f"Face recognized as: {name}")
