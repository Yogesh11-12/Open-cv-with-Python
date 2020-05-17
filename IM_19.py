import cv2
def sketch(img):
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_gray_blur=cv2.bilateralFilter(img_gray,9,75,75)
    canny_edge=cv2.Canny(img_gray_blur,10,90)
    ret,mask=cv2.threshold(canny_edge,70,255,cv2.THRESH_BINARY)
    return mask
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    cv2.imshow("livewebcam",sketch(frame))
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows
