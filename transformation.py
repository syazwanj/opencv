import cv2 as cv
import numpy as np

#Reading images
path = 'C:\\Users\\Syazwan\\OneDrive\\Pictures\\'
img = cv.imread(path+'runners.jpg')
cv.imshow('Syazwan',img)

#Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> up
# +x --> right
# +y --> down

translated = translate(img,-100,100)
cv.imshow('translated',translated)

#Rotation
def rotate(img,angle,rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img,-45)
cv.imshow('rotated',rotated)

rotated_rotated = rotate(img,-90)
cv.imshow('rotated rotated', rotated_rotated)

#resizing
resized = cv.resize(img, (500,500),interpolation = cv.INTER_AREA)
cv.imshow('resized',resized)

#Flipping
flip = cv.flip(img, -1) #0 is flip vertically, 1 is flip horizontally. -1 is both.
cv.imshow('flip',flip)

#Cropping
cropped = img[200:600,300:900]
cv.imshow('cropped',cropped)


cv.waitKey(0)