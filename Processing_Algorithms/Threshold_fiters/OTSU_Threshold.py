import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('Photos\WIN_20170102_20_34_33_Pro.jpg', 0)
# 0 in the second argument is for grayscale
img = img[150:300,150:350]
img = cv2.medianBlur(img, 5)
ret,th = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
images = [img, th]
for i in xrange(2):
    plt.subplot(2,1,i+1),plt.imshow(images[i],'gray')
    plt.xticks([]), plt.yticks([])
plt.show()
