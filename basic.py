import cv2 as cv

#Reading images
path = 'C:\\Users\\Syazwan\\OneDrive\\Pictures\\'
img = cv.imread(path+'runners.jpg')
cv.imshow('Syazwan',img)

#Converting to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

#Edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny',canny)

#Dilating the image
dilated = cv.dilate(canny, (7,7),iterations = 3)
cv.imshow('dilated',dilated)

#Eroding gets back the edge cascade from the dilated image
eroded = cv.erode(dilated, (7,7),iterations = 3)
cv.imshow('eroded',eroded)

#Resize
resized = cv.resize(img, (500,500),interpolation=cv.INTER_AREA) #area for making smaller, linear and cubic for bigger
cv.imshow('resized',resized)

#Cropping
cropped = img[50:200,200:400]
cv.imshow('cropped',cropped)



cv.waitKey(0)