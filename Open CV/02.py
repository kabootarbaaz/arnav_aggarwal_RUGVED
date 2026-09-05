import cv2 as cv
a = cv.imread(r"C:\Users\Asus\Pictures\real.jpg")
resize= cv.resize(a,(250,250))
cv.imshow('real',a)
cv.imshow("Resized Image",resize)
crop=a[20:200 , 20:200]
cv.imshow("Cropped Image",crop)
(h,w)=a.shape[:2]
center=(w//2,h//2)
B=cv.getRotationMatrix2D(center,180,1.0)
rotated=cv.warpAffine(a,B,(w,h))
flip=cv.flip(a,0)
cv.imshow("Flipped",flip)
cv.imshow("Rotated Image",rotated)
cv.waitKey(0)
cv.destroyAllWindows()