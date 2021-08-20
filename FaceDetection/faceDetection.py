import cv2 as cv

img = cv.imread("Photos/caras.jpg")
cv.imshow("Person", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Person", gray)

haar_cascade = cv.CascadeClassifier("haar_face.xml")

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
#print(faces_rect)

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    #print(x+(h/2))
    cv.imshow("hola",img)

cv.waitKey(0)
