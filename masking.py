import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#Reading images
path = 'C:\\Users\\Syazwan\\OneDrive\\Pictures\\'
img = cv.imread(path+'runners.jpg')
img = cv.resize(img, (img.shape[1]//3,img.shape[0]//3),interpolation=cv.INTER_AREA) #area for making smaller, linear and cubic for bigger
cv.imshow('Syazwan',img)

blank = np.zeros(img.shape[:2],dtype = 'uint8')
#cv.imshow('Blank Image',blank)

mask = cv.rectangle(blank, (img.shape[1]//2,img.shape[0]//2), (img.shape[1]//2 + 100,img.shape[0]//2 +100), 255,thickness = -1)
cv.imshow('Mask',mask)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, thickness = -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, thickness = -1)
weird_shape = cv.bitwise_xor(circle, rectangle)
cv.imshow('Weird Shape', weird_shape)

masked = cv.bitwise_and(img, img,mask=weird_shape)
cv.imshow('Weird Shape Masked Image',masked)

cv.waitKey(0)