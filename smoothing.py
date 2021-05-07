import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#Reading images
path = 'C:\\Users\\Syazwan\\OneDrive\\Pictures\\'
img = cv.imread(path+'runners.jpg')
img = cv.resize(img, (img.shape[1]//3,img.shape[0]//3),interpolation=cv.INTER_AREA) #area for making smaller, linear and cubic for bigger
cv.imshow('Syazwan',img)

#Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average blur',average)

#Gaussian blur
gauss = cv.GaussianBlur(img, (3,3), 0) #sigmaX is the std in x-dirn
cv.imshow('Gaussian Blur',gauss)

#Median blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur',median)

#Bilateral
#Sigma space: By giving larger values, means u want pixels further away to influence the center pixel
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)



cv.waitKey(0)