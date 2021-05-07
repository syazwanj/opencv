import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#Reading images
path = 'C:\\Users\\Syazwan\\OneDrive\\Pictures\\'
img = cv.imread(path+'runners.jpg')
img = cv.resize(img, (img.shape[1]//3,img.shape[0]//3),interpolation=cv.INTER_AREA) #area for making smaller, linear and cubic for bigger
cv.imshow('Syazwan',img)

blank = np.zeros(img.shape[:2],dtype = 'uint8')

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)
print(img.shape) #the '3' represent the number of colour channels
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged image', merged)

cv.waitKey(0)