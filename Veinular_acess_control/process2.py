import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('temp.jpg',0)
#img = img[150:300,150:350]
kernel = np.ones((5,5), np.uint8)
# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(7,7))
cl1 = clahe.apply(img)
# perform blur
cl2 = cv2.medianBlur(cl1, 5)
blur = cv2.GaussianBlur(cl1,(5,5),0)
# thresholding - otsu and adaptive
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
th1 = cv2.adaptiveThreshold(cl2,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,25,2.55)
#remove noise
th2 = th1 & th3
#morphological transform
opening = cv2.morphologyEx(th2, cv2.MORPH_OPEN, kernel)
#save the images
cv2.imwrite('temp.jpg',opening)
