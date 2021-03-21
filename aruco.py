#start but not work

import numpy as np 
import cv2 
import cv2.aruco as aruco 
import sys, time, math 

#---Define Tag
id_to_find = 72
marker_size = 10 #-[cm]

#---Get the camera calibration path
calib_path = ""
camera_matrix = np.loadtxt(calib_path+'calFiles/cameraMatrix.txt', delimiter=',')
camera_distortion = np.loadtxt(calib_path+'calFiles/cameraDistortion.txt', delimiter=',')

#---180degree rotation matrix around the x axis
R_flip = np.zeros((3,3), dtype=np.float32)
R_flip[0,0] = 1.0
R_flip[1,1]=-1.0
R_flip[2,2] =-1.0

#---Define the aruco dictionary
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_ARUCO_ORIGINAL)
parameters = aruco.DetectorParameters_create()

#---Capture the videocamera 
cap = cv2.VideoCapture(0)
#---Set cam size 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret, frame =cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    corners, ids, rejected = aruco.detectMarkers(image=gray, dictionary=aruco_dict, 
    parameters=parameters) 

    if ids != None and ids[0] == id_to_find:
        ret = aruco.estimatePoseSingleMarkers(corners, marker_size, camera_matrix, camera_distortion)

        #-- Unpack the output, get only the first 
        rvec, tvec =ret[0][0,0,:], ret[1][0,0,:]

        #-- Draw the detect marker and put a refernce frame over it
        aruco.drawDetectMarkers(frame, corners)
        aruco.drawAxis(frame, camera_matrix, camera_distortion, rvec, tvec, 10)
    
    #-- Display the frame
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
    








