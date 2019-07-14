import numpy as np
from matplotlib import pyplot as plt
import cv2
from pylab import array, show, axis, arange, figure, uint8

img = cv2.imread('img.jpg', 0)
# 0 in the second argument is for grayscale
img = cv2.medianBlur(img, 5)
maxIntensity = 255.0 # depends on dtype of image data
x = arange(maxIntensity)

# Parameters for manipulating image data
phi = 1
theta = 1
newImage1 = (maxIntensity/phi)*(img/(maxIntensity/theta))**2
newImage1 = array(newImage1,dtype=uint8)
z = (maxIntensity/phi)*(x/(maxIntensity/theta))**2

cv2.imshow('img', img)
cv2.imshow('newImage', newImage1)
cv2.imwrite('improvedcontrast.jpg',newImage1)
cv2.waitKey(0)
cv2.destroyAllWindows()


