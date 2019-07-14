
import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('test.jpg',0)          # queryImage
img2 = cv2.imread('temp.jpg',0) # trainImage

# Initiate surf object with default values
surf = cv2.xfeatures2d.SURF_create(400)
surf.setHessianThreshold(40000)

surf.setUpright(True)
# find the keypoints and descriptors with surf
kp1, des1 = surf.detectAndCompute(img1,None)
kp2, des2 = surf.detectAndCompute(img2,None)
# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)
# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
# cv2.drawMatchesKnn expects list of lists as matches.
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,2)
plt.imshow(img3),plt.show()

