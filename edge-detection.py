import cv2 as cv
import numpy as np

cv.startWindowThread()

img = cv.imread('tree.jpg')
edges = cv.Canny(img, 100, 200) # (image, lower pixel value, higher pixel value)

cv.imshow('', edges)
cv.waitKey()
cv.destroyAllWindows()