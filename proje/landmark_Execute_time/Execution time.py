import timeit
import time
from PIL import Image, ImageDraw
import face_recognition
import cv2

start_time = time.time()


process_this_frame = True

image = face_recognition.load_image_file('landmark_Execute_time\\images\\two_people.jpg')

face_landmarks_list = face_recognition.face_landmarks(image)

print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))
pil_image = Image.fromarray(image)
drew = ImageDraw.Draw(pil_image)
if process_this_frame:
    face_locations = face_recognition.face_locations(image)

for (top, right, bottom, left), in zip(face_locations):
    drew.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))


for face_landmarks in face_landmarks_list:

    for facial_feature in face_landmarks.keys():
        drew.line(face_landmarks[facial_feature], width=5)


cv2.waitKey(1)


cv2.destroyAllWindows()

pil_image.save('landmark_Execute_time/result/two_people.png')

end_time = time.time()
Execution_time = end_time-start_time
ex = round(Execution_time, 2)
f = open('landmark_Execute_time\\result\\two__people.txt', 'a')
f.write('Execution time:'+str(ex)+'s')
f.close()
# ***********************************************************************************
