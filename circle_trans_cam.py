#NOT START
import cv2
import numpy as np 


cap = cv2.VideoCapture(0)   # usb port number

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        
         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
         img	= cv2.medianBlur(gray,	5)
         cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
        
         circles	= cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,1,120,param1=100,param2=30,minRadius=0,maxRadius=0)
         circles	= np.uint16(np.around(circles))

         for i in circles[0,:]:
			
			         cv2.circle(cap,(i[0],i[1]),i[2],(0,255,0),6)		
		             cv2.circle(cap,(i[0],i[1]),2,(0,0,255),2)

         cv2.imshow('frame', cap)
    
         if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.realease()
cv2.destroyAllWindows()


