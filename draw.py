import cv2 as cv
import numpy as np

blank = np.zeros((400,400,3), dtype = 'uint8') #uint8 is the dat type of img
cv.imshow('Blank',blank)

path = 'C:\\Users\\Syazwan\\OneDrive\\Pictures\\'
img = cv.imread(path+'syazwan.jpg')
#cv.imshow('Syazwan',img)

#1. Print the image a certain colour
blank[200:300,300:400] = 0,255,0
#cv.imshow('Green',blank)

#2. Draw a rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,0,0),thickness=cv.FILLED) #var, pt1, pt2, colour, thickness of the shape
cv.imshow('Rectangle',blank)

#3. Draw a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness = -3)
cv.imshow('Circle',blank)

#4. Draw a line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),color = (255,255,255),thickness=3)
cv.imshow('Line',blank)

#5. Write text
cv.putText(blank,'Hello motherfucker',(30,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,255),thickness=2)
cv.imshow('Text',blank)

cv.waitKey(0)