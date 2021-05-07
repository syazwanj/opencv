import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#Reading images
path = 'C:\\Users\\Syazwan\\OneDrive\\Pictures\\'
img = cv.imread(path+'runners.jpg')
cv.imshow('Syazwan',img)

# plt.imshow(img)
# plt.show()

#BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#BGR to HSV (Hue, saturation, value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

#BGR to LAB (L x a x b)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)
# plt.imshow(rgb)
# plt.show()

#HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV ---> BGR', hsv_bgr)

#LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB ---> BGR', lab_bgr)


cv.waitKey(0)