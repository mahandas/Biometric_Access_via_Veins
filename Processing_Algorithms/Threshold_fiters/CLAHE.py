import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img.jpg',0)

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
images = [img, cl1]
for i in xrange(2):
    plt.subplot(2,1,i+1),plt.imshow(images[i],'gray')
    plt.xticks([]), plt.yticks([])
plt.show()
cv2.destroyAllWindows()
