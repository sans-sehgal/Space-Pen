import cv2
import numpy as np 

def empty(a):
	pass


cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars' , 640,240)

cv2.createTrackbar('Hue Min' , 'Trackbars', 46, 179,empty)
cv2.createTrackbar('Hue Max' , 'Trackbars', 164, 179,empty)
cv2.createTrackbar('Sat Min' , 'Trackbars', 53, 255,empty)
cv2.createTrackbar('Sat Max' , 'Trackbars', 131, 255,empty)
cv2.createTrackbar('Val Min' , 'Trackbars', 76, 255,empty)
cv2.createTrackbar('Val Max' , 'Trackbars', 160, 255,empty)


cap=cv2.VideoCapture(0)

while True:
	success , img=cap.read()
	img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	h_min=cv2.getTrackbarPos('Hue Min' , 'Trackbars')
	h_max=cv2.getTrackbarPos('Hue Max' , 'Trackbars')
	s_min=cv2.getTrackbarPos('Sat Min' , 'Trackbars')
	s_max=cv2.getTrackbarPos('Sat Max' , 'Trackbars')
	v_min=cv2.getTrackbarPos('Val Min' , 'Trackbars')
	v_max=cv2.getTrackbarPos('Val Max' , 'Trackbars')
	#print(h_min,h_max,s_min,s_max,v_min,v_max)
	lower=np.array([h_min,s_min,v_min])
	upper=np.array([h_max,s_max,v_max])
	mask=cv2.inRange(img_hsv,lower,upper)
	imgResult=cv2.bitwise_and(img,img,mask=mask)
	cv2.imshow('Res',img)
	cv2.imshow('love1' , imgResult)
	cv2.imshow('mask' , mask)


	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
