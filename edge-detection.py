import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('tree.jpg')
edges = cv.Canny(img, 50, 100) # (image, lower pixel value, higher pixel value)

cv.imshow('', edges)