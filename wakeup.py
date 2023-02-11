import cv2
import os
from pygame import mixer
import time
import numpy as np
import dlib
import matplotlib.pyplot as plt
from PIL import Image
import statistics

root_dir = "/users/YOUR_USERNAME_HERE/documents/sleepwatcher"

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('%s/shape_predictor_68_face_landmarks.dat' % root_dir)

def image_has_glasses(path="%s/capture.jpg" % root_dir):
    img = dlib.load_rgb_image(path)
    
    if len(detector(img))==0:
        return -1
    rect = detector(img)[0]
    sp = predictor(img, rect)
    landmarks = np.array([[p.x, p.y] for p in sp.parts()])

    nose_bridge_x = []
    nose_bridge_y = []

    for i in [28,29,30,31,33,34,35]:
        nose_bridge_x.append(landmarks[i][0])
        nose_bridge_y.append(landmarks[i][1])

    ### x_min and x_max
    x_min = min(nose_bridge_x)
    x_max = max(nose_bridge_x)

    ### ymin (from top eyebrow coordinate),  ymax
    y_min = landmarks[20][1]
    y_max = landmarks[30][1]

    img2 = Image.open(path)
    img2 = img2.crop((x_min,y_min,x_max,y_max))

    img_blur = cv2.GaussianBlur(np.array(img2),(3,3), sigmaX=0, sigmaY=0)

    edges = cv2.Canny(image =img_blur, threshold1=100, threshold2=200)

    edges_center = edges.T[(int(len(edges.T)/2))]

    if 255 in edges_center:
        return(True)
    else:
        return(False)


cap = cv2.VideoCapture(0)

# let the camera warm up
time.sleep(3)
# output image
ret, frame = cap.read()
path = "%s/capture.jpg" % root_dir
sound = "%s/qinaide.mp3" % root_dir

out = cv2.imwrite(path, frame)
# wait a second
time.sleep(1)
# run detection
wears_glasses = image_has_glasses(path=path)
if not wears_glasses:
    # play mp3
    mixer.init()
    mixer.music.load(sound)
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)

# close everything and remove the image file
os.remove(path)
cap.release()
cv2.destroyAllWindows()