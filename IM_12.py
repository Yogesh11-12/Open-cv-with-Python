import cv2
import numpy as np
img=cv2.imread('C:/Users/yogesh yadav/Desktop/lena.jpg')
cv2.imshow('LENA_original',img)
cv2.waitKey(0)
a=np.ones(img.shape,dtype="uint8")*100
added=cv2.add(img,a)
cv2.imshow("added",added)
cv2.waitKey(0)
multi=cv2.multiply(img,a)
cv2.imshow("muultiply",multi)
cv2.waitKey(0)
cv2.destroyAllWindows()
