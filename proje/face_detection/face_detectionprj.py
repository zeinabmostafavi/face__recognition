import face_recognition
import cv2
import numpy as np


process_this_frame = True

frame = cv2.imread('face_detection/images/bando.jpg')

small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

rgb_small_frame = small_frame[:, :, ::-1]

if process_this_frame:
    face_locations = face_recognition.face_locations(rgb_small_frame)
# Display the results
for (top, right, bottom, left), in zip(face_locations):
    top *= 3
    right *= 4
    bottom *= 4
    left *= 4

    cv2.rectangle(frame, (left, top), (right, bottom), (40, 100, 255), 8)


cv2.imwrite('face_detection/result/bando.png', frame)

cv2.waitKey(1)


cv2.destroyAllWindows()
