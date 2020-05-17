import cv2
import numpy as np

img=cv2.imread('C:/Users/yogesh yadav/Desktop/lena.jpg',0)
cv2.imshow('LENA',img)
cv2.waitKey(0)
height,width=img.shape
sobel_x=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobel_y=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
sobel=cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow("sobelfilter",sobel)
cv2.waitKey(0)
lap=cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow("laplacian",lap)
cv2.waitKey(0)
canny=cv2.Canny(img,25,200)
cv2.imshow("cannyfilter",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
