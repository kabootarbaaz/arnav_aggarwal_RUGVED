import cv2 as cv
a = cv.imread(r"C:\Users\Asus\Pictures\real.jpg")
cv.imshow('real',a)
gray=cv.cvtColor(a,cv.COLOR_BGR2GRAY)
hsv=cv.cvtColor(a,cv.COLOR_BGR2HSV)
cv.imshow('Grayschale Image',gray)
cv.imshow("HSV image",hsv)
edges = cv.Canny(a, 100, 200)
cv.imshow('Edges', edges)
cv.waitKey(0)
cv.destroyAllWindows