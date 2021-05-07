import cv2 as cv
import numpy as np
import socket

#Reading images
path = 'C:\\Users\\Syazwan\\OneDrive\\Pictures\\'
img = cv.imread(path+'runners.jpg')
cv.imshow('Syazwan',img)

blank = np.zeros(img.shape,dtype = 'uint8')
cv.imshow('Blank',blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)

canny = cv.Canny(img,125,175)
cv.imshow('Canny',canny)


ret, thresh = cv.threshold(gray, 95, 255, cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)


contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#contours is a list of all the contours in the image
#hierarchies is the representation that opencv uses to find these contours
#chain approx none does nothing, returns all the contours
#chain approx simple compresses the contours into two points
#since contours is a list, we can find the number of contours found by printing the length of the list

print(f'{len(contours)} contour(s) found')

#Draw the contours onto the blank image. -1 means all the contours, then pass the colour and thickness.
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)


cv.waitKey(0)