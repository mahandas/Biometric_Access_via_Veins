import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img.jpg',0)

img1 = cv2.medianBlur(img, 7)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(img1,None)

simg = cv2.drawKeypoints(img1,kp,cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


images = [img,img1,simg]
for i in xrange(3):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
plt.show()

