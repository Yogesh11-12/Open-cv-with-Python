import cv2
img=cv2.imread('C:/Users/yogesh yadav/Desktop/lena.jpg')
cv2.imshow('Yogesh',img)
print(img.shape)
print("Height of the image: ",img.shape[0])
print("width of the image: ", img.shape[1])
cv2.waitKey(0)
cv2.destroyAllWindows()
