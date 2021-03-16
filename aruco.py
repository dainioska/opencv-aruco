import numpy as np 
import cv2 
import cv2.aruco as aruco 
import sys, time, math 

#---Define Tag
id_to_fin = 72
marker_size = 10 #-[cm]

#---Get the camera calibration path
calib_path = ""
camera_matrix = np.loadtxt(calib_path+'cameraMatrix.txt', delimiter=',')
camera_distortion = np.loadtxt(calib_path+'cameraDistortion.txt', delimiter=',')

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
#---Set cam size as the one it was calibrated with
###
while True:
    ret, frame =cap.read()