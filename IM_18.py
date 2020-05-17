import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    L_r=np.array([0,25,0])
    H_r=np.array([255,255,255])
    mask=cv2.inRange(hsv,L_r,H_r)
    cv2.imshow("HSV",hsv)
    cv2.imshow("livewebcam",frame)
    cv2.imshow("masking",mask)
    
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows
