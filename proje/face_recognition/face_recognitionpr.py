import face_recognition
import cv2
import numpy as np

obama_image = face_recognition.load_image_file(
    "face_recognition/images/obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

biden_image = face_recognition.load_image_file(
    "face_recognition/images/biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding
]
known_face_names = [
    "Barack Obama",
    "Joe Biden"
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

pic = cv2.imread('face_recognition/images/two_people.jpg')

small_frame = cv2.resize(pic, (0, 0), fx=0.25, fy=0.25)

rgb_small_frame = small_frame[:, :, ::-1]

if process_this_frame:
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(
        rgb_small_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(
            known_face_encodings, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(
            known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

process_this_frame = not process_this_frame

# Display the results
for (top, right, bottom, left), name in zip(face_locations, face_names):
    top *= 3
    right *= 4
    bottom *= 5
    left *= 4

    cv2.rectangle(pic, (left, top), (right, bottom), (40, 100, 255), 8)

    cv2.rectangle(pic, (left, bottom - 35),
                  (right, bottom), (125, 0, 255), cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(pic, name, (left + 6, bottom - 6), font, 0.62, (0, 0, 0), 2)

cv2.imwrite('face_recognition/result/two_people.png', pic)

cv2.waitKey(1)


cv2.destroyAllWindows()
