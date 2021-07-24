import cv2
import numpy as np

cap=cv2.VideoCapture(0)

cap.set(10,150)


myColors=[
		  [31,29,56,94,255,97]]
vals=[[0,255,0]]

myPoints = []


def findColor(img,myColors,vals):
	img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	count=0
	newPoints=[]
	for color in myColors:
		lower=np.array(color[0:3])
		upper=np.array(color[3:6])
		mask=cv2.inRange(img_hsv,lower,upper)
		x,y=getContours(mask)
		cv2.circle(img_result,(x,y), 10,vals[count], cv2.FILLED)
		count+=1
		cv2.imshow(str(color[0]),mask)
		if x!=0 and y!=0:
			newPoints.append([x,y,count-1])
	return newPoints


def getContours(img):
	contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	x,y,w,h=0,0,0,0
	for cnt in contours:
		area=cv2.contourArea(cnt)
		#print(area)
		if area > 1000:
			#cv2.drawContours(img_result,cnt,-1,(0,255,0) ,3)
			peri=cv2.arcLength(cnt,True)
			approx=cv2.approxPolyDP(cnt, 0.02*peri,True)
			x,y,w,h=cv2.boundingRect(approx)
	return x+w//2,y

def drawOnCanvas(myPoints,vals):
	for point in myPoints:
		cv2.circle(img_result,(point[0],point[1]), 10,vals[point[2]], cv2.FILLED)





while True:
	success , img=cap.read()
	img=cv2.flip(img,1)
	img_result=img.copy()
	print(vals[0])
	newPoints=findColor(img,myColors,vals)
	if len(newPoints)!=0:
		for newp in newPoints:
			myPoints.append(newp)
	# #print(myPoints)
	if len(myPoints)!=0:
		drawOnCanvas(myPoints,vals)


	cv2.imshow('Res',img_result)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	