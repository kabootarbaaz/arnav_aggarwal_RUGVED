import cv2 as cv
a = cv.imread(r"C:\Users\Asus\Pictures\real.jpg")
cv.imshow('real',a) #show the img
cv.waitKey(0) #open window
cv.destroyAllWindows() # close window
h,w,c=a.shape
print("Height:",h,"\n Width:",w,"\n Channels:",c)
cv.imwrite("new.jpg", a)