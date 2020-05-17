import cv2
import numpy as np
img=cv2.imread('C:/Users/yogesh yadav/Desktop/lena.jpg')
cv2.imshow('LENA_original',img)
height,width=img.shape[:2]
nh,nw=height/4,width/4

T=np.float32([[1,0,nw],[0,1,nh]])
img_t=cv2.warpAffine(img,T,(width,height))
cv2.imshow("Translation",img_t)
cv2.waitKey(0)
cv2.destroyAllWindows()
