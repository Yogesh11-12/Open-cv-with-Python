import cv2
import numpy as np
img=cv2.imread('C:/Users/yogesh yadav/Desktop/lena.jpg')
cv2.imshow('LENA_original',img)
B,G,R=cv2.split(img)
Zeros=np.zeros(img.shape[:2],dtype='uint8')
cv2.imshow("red",cv2.merge([Zeros,Zeros,R]))

cv2.waitKey(0)
cv2.destroyAllWindows()
