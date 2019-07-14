import numpy as np
import cv2
from matplotlib import pyplot as plt
from timeit import default_timer

img = cv2.imread('temp.jpg',0)
start = default_timer()

# Initiate ORB detector
orb = cv2.ORB_create()
# find the keypoints with ORB
kp = orb.detect(img,None)

# compute the descriptors with ORB
kp, des = orb.compute(img, kp)
duration=default_timer() - start
print duration
# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)
plt.imshow(img2), plt.show()
