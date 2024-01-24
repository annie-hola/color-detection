import cv2
from PIL import Image # PIL : Python Image Library - Pillow
from utils import get_limits


yellow = [0, 255, 255] # BGR

cap = cv2.VideoCapture(0)
'''
0: Default camera (usually the built-in webcam on most laptops)
1: Second camera (if available)
2, 3, and so on: Additional cameras or devices
'''

# run loop to capture video frame
while True:
    _, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # get all shade of yellow

    lowerLimit, upperLimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)
    
    # draw border box
    bbox = mask_.getbbox() 
    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5) #draw rectangle tracking for each frame

    cv2.imshow('frame', frame) # open frame camera

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
