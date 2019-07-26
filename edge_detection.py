import cv2 as cv
import numpy as np

img = cv.imread('images/tush.jpg')
edges = cv.Canny(img, 50, 100) # (image, lower pixel value, higher pixel value)

while True:
    cv.imshow('', edges)
    
    if cv.waitKey(0) == ord('q'):
        break
        
cv.destroyAllWindows()
