import cv2
import os

for i, entry in enumerate(os.scandir('landmark_Execute_time/images/')):
    a = entry.path
    name = cv2.imread(a)
    if name is None:
        continue
    idx = a.rfind('/')
    a = a[idx + 1:]

    index = a.rfind('.')

    c = a[:index]
    cv2.imwrite(f'landmark_Execute_time/result/{c}.png', name)

    with open(f'landmark_Execute_time/result/{c}.txt', mode='w') as file:

        file.write(f'I am an image.\nMy name is {a}')
