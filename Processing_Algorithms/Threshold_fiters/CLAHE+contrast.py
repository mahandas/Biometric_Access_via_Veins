import numpy as np
import cv2
from pylab import array, show, axis, arange, figure, uint8

img = cv2.imread('img.jpg',0)
# img = cv2.medianBlur(img, 5)
maxIntensity = 255.0 # depends on dtype of image data
x = arange(maxIntensity)
# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(4,4))
cl1 = clahe.apply(img)
phi = 1
theta = 0.9
newImage1 = (maxIntensity/phi)*(cl1/(maxIntensity/theta))**2
newImage1 = array(newImage1,dtype=uint8)
res = np.hstack((img,cl1)) #stacking images side-by-side
cv2.imshow('clahe',res)
cv2.imshow('contrast adjusted', newImage1)
cv2.waitKey(0)
cv2.destroyAllWindows()
