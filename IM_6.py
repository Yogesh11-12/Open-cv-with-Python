import cv2
img=cv2.imread('C:/Users/yogesh yadav/Desktop/lena.jpg')
cv2.imshow('LENA',img)
hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV image",hsv_img)
cv2.imshow("Hue",hsv_img[:,:,0])
cv2.imshow("Saturation",hsv_img[:,:,1])
cv2.imshow("Values",hsv_img[:,:,2])

cv2.waitKey(0)
cv2.destroyAllWindows()
