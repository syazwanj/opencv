import cv2 as cv

path = 'C:\\Users\\Syazwan\\OneDrive\\Pictures\\'
img  = cv.imread(path+'syazwan.jpg')
cv.imshow('Syazwan',img)


def rescaleFrame(frame, scale=0.5):
    #Images, videos and live video
    width = int(frame.shape[1]*scale) #this is the width of img
    height = int(frame.shape[0]*scale) #this is height of img in px
    dimensions = (width,height)
    print(dimensions)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)
resized_image = rescaleFrame(img)
cv.imshow('Rescaled image',resized_image)

def changeRes(width,height):
    #Only live video (e.g. webcam, ext camera)
    capture.set(3,width) #3 references width
    capture.set(4,height) #4 references height of this capture obj

#Reading videos
capture = cv.VideoCapture('C:\\Users\\Syazwan\\Downloads\\steveryan_nowatermark01.mp4')
while True:
    isTrue, frame = capture.read() #read the video frame by frame
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video',frame) #display each frame of the video
    cv.imshow('Video Resized',frame_resized)
    if cv.waitKey(20) & 0xFF ==ord('d'): #if the letter 'd' is pressed, break the loop
        break

capture.release() #Release the capture device and destroy the windows
cv.destroyAllWindows()

cv.waitKey(0)