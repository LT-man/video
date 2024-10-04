import cv2
import os
from PIL import Image
path = "C:/Users/laury/Documents/jetlearn/opencv/lesson 6/Video"
#change directory or folder
os.chdir(path)
print(os.listdir("."))
images = os.listdir(".")
sumw = 0
sumh = 0
for image in images: 
    img = Image.open(path + "/" + image)
    w, h = img.size
    sumw = sumw + w
    sumh = sumh + h
n = len(images)
avgw = sumw // n
avgh = sumh // n
for image in images:
    img = Image.open(path + "/" + image)
    imgresize = img.resize((avgw, avgh))
    imgresize.save(image, "JPEG", quality = 90)
#converting to video
myvideo = "myvideo.avi"
frame = cv2.imread(path + "/" + images[0])
video = cv2.VideoWriter(myvideo, 0, 0.25, (avgw, avgh))
for image in images:
    video.write(cv2.imread(path + "/" + image))
video.release()