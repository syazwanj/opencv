import cv2 as cv

#Reading images
path = 'C:\\Users\\Syazwan\\OneDrive\\Pictures\\'
img = cv.imread(path+'syazwan.jpg')
#cv.imshow('Syazwan',img)

#Reading videos
capture = cv.VideoCapture('C:\\Users\\Syazwan\\Downloads\\steveryan_nowatermark01.mp4')
while True:
    isTrue, frame = capture.read() #read the video frame by frame
    cv.imshow('Video',frame) #display each frame of the video
    if cv.waitKey(20) & 0xFF ==ord('d'): #if the letter 'd' is pressed, break the loop
        break

capture.release() #Release the capture device and destroy the windows
cv.destroyAllWindows()