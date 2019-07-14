import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('img.jpg', 0)
# 0 in the second argument is for grayscale
img = img[150:300,150:350]
th1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                            cv2.THRESH_BINARY,11,2)

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                            cv2.THRESH_BINARY,11,2)
titles = ['Original', 'Adaptive Mean', 'Adaptive Gaussian']
images = [img, th1, th2]

for i in xrange(3):
    plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
plt.show()



