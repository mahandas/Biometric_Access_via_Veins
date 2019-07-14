import numpy as np
import cv2
import operator
import sys

limit=sys.argv[1]
img1 = cv2.imread('temp.jpg',0)          # queryImage
# Initiate ORB detector
orb = cv2.ORB_create()
# find the keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img1,None)

n = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in xrange(1,int(limit)):
    img2=cv2.imread(str(i) + '.jpg') # trainImage
    
    # find the keypoints and descriptors with ORB
    kp2, des2 = orb.detectAndCompute(img2,None)
  
    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    # Match descriptors.
    matches = bf.match(des1,des2)
    n[i]=len(matches)
    #print n[i]
    
index, value = max(enumerate(n), key=operator.itemgetter(1))
y=index
print y
if n[index] < 50:
    print "No match Found"
    y = 0
dfile = open('match.txt', 'w+')
dfile.write("%d" %y)
dfile.close()
