# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

def nothing(x):
    pass
cap = cv2.VideoCapture(0)
# Create a window
cv2.namedWindow('image')

# create trackbars for color change
#cv2.createTrackbar('CLimit','image',0,8,nothing)

img1 = cv2.imread('out.jpg')
rows,cols,channels = img1.shape

img2gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
#for contours
#image, contours, hierarchy = cv2.findContours(img2gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    roi = image[0:rows, 0:cols ]

    # Our operations on the frame come here

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    
   
    # Display the resulting frame

    dst = cv2.addWeighted(gray, 0.8, img2gray, 0.2, 0)
    #for contours
    #dst = cv2.drawContours(gray, contours, 4, (0,0,255), 1)
    cv2.imshow("image",dst)
    k = cv2.waitKey(1) & 0xFF

    if k == ord("a"):
            cv2.imwrite(time.strftime("Screenshot%Y%m%d%H%M%S.jpg"),cl1)
            break
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if k == ord("q"):
            break
  

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

