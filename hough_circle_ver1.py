#ver1
import numpy as np
import argparse
import cv2
import time

cap = cv2.VideoCapture(0) 

while(True):
	ret, frame = cap.read()
			
	output = frame.copy()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray,(5,5),0)
	gray = cv2.medianBlur(gray,5)
	gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,3.5)
	
	kernel = np.ones((2,3),np.uint8)
	gray = cv2.erode(gray,kernel,iterations = 1)
	gray = cv2.dilate(gray,kernel,iterations = 1)
	circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 200, param1=30, param2=45, minRadius=0, maxRadius=0)
	
	if circles is not None:
		circles = np.round(circles[0, :]).astype("int")
		
		for (x, y, r) in circles:
			
			cv2.circle(output, (x, y), r, (0, 255, 0), 4)
			cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
			#time.sleep(0.1)
			print "Column Number: "
			print x
			print "Row Number: "
			print y
			print "Radius is: "
			print r

		#cv2.imshow('gray',gray)
    	cv2.imshow('frame',output)
 	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
