import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

img = cv.imread('images/wallplants.jpg')
ir, ir_n_g, ir_n_r = cv.split(img)

ndvi = (ir + ir - ir_n_r)/(ir_n_r)

cv.imshow('', ndvi)