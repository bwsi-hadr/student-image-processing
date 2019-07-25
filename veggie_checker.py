import cv2 as cv
import numpy as np
from PIL import Image

cv.startWindowThread()

img = Image.open('images/wallplants.jpg')
img = np.array(img)
ir, ir_n_g, ir_n_r = cv.split(img)

ndvi = (ir + ir - ir_n_r)/(ir_n_r)

cv.imshow('', ndvi)
cv.waitKey()
cv.destroyAllWindows()
