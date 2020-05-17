import cv2
import numpy as np
img=cv2.imread('C:/Users/yogesh yadav/Desktop/lena.jpg')
cv2.imshow('LENA_original',img)
img_scaling=cv2.resize(img,None,fx=0.75,fy=0.75)
cv2.imshow("resize",img_scaling)
img_double=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imshow("Double",img_double)
cv2.waitKey(0)
img_scaled=cv2.resize(img,(800,400),interpolation=cv2.INTER_AREA)
cv2.imshow("pixelwise",img_scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()
