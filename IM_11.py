import cv2
import numpy as np
img=cv2.imread('C:/Users/yogesh yadav/Desktop/lena.jpg')
cv2.imshow('LENA_original',img)
cv2.waitKey(0)
height,width=img.shape[:2]
start_raw,start_cols=int(height*.20),int(width*.20)
end_raw,end_cols=int(height*.8),int(width*.8)
cropped=img[start_raw:end_raw,start_cols:end_cols]
cv2.imshow("cropped image",cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
