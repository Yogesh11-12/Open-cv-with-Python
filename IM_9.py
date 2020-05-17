import cv2
import numpy as np
img=cv2.imread('C:/Users/yogesh yadav/Desktop/lena.jpg')
cv2.imshow('LENA_original',img)
height,width=img.shape[:2]
rotate=cv2.getRotationMatrix2D((width/2,height/2),90,0.5)
img_t=cv2.warpAffine(img,rotate,(width,height))
cv2.imshow("rotation",img_t)
cv2.waitKey(0)
cv2.destroyAllWindows()
