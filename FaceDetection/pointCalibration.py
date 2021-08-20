import cv2 as cv
import numpy as np
import math

capture = cv.VideoCapture(0)

def rescaleFrame(frame, scale=0.75):  # Rescalar el video (Default = 0.75) 
    width = int(frame.shape[1]  * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) # Que es el INTER_AREA ???

while True:
    isTrue, frame1 = capture.read(0)
    frame1 = cv.flip(frame1, 1)
    frame1 = rescaleFrame(frame1, 1) #cambiar el valr aca para aumentar o achicar

    width = int(frame1.shape[1])
    height = int(frame1.shape[0])

    cv.imshow('pointCalibration', frame1)

    if cv.waitKey(19) & 0xFF==ord("f"):  # Tecla "d" para romper el while
        break

capture.release()
cv.destroyAllWindows()
