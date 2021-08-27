import face_recognition
import cv2

image = face_recognition.load_image_file('text_landmark\\images\\two_people.jpg')
face_locations = face_recognition.face_locations(image)
face_landmarks_list = face_recognition.face_landmarks(image)

f = open('text_landmark\\result\\two__people.txt', 'a')
f.write('There are '+str(format(len(face_locations)))+' face''s  in image\n')
f.write('----------------------------------------\n')
f.write('face number 1:\n')
f.write('Locations:\n')
f.write(str(face_locations[0])+'\n')

f.write('Landmarks:\n')
f.write(str(face_landmarks_list[0])+'\n')
f.write('----------------------------------------\n')
f.write('face number 2:\n')
f.write('Locations:\n')
f.write(str(face_locations[1])+'\n')
f.write('Landmarks:\n')
f.write(str(face_landmarks_list[1])+'\n')

f.close()
