import cv2
img=cv2.imread('C:/Users/yogesh yadav/Desktop/lena.jpg')
cv2.imshow('LENA',img)
Gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale',Gray_img)


cv2.waitKey(0)
cv2.destroyAllWindows()
