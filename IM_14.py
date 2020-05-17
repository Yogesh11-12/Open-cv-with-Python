import cv2
import numpy as np

img=cv2.imread('C:/Users/yogesh yadav/Desktop/lena.jpg')
cv2.imshow('LENA',img)
cv2.waitKey(0)
kernel=np.zeros((5*5),np.float32)/25
blur=cv2.filter2D(img,-1,kernel)
cv2.imshow("blured",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
