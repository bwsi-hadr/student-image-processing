import cv2 as cv
import numpy as np
from PIL import Image

cv.startWindowThread()

img = Image.open('images/tush.jpg')
img = np.array(img)
ir, ir_n_g, ir_n_r = cv.split(img)

bottom = ir_n_r.astype(float)
bottom[bottom == 0] = 0.01

ndvi = ((ir + ir).astype(float) - ir_n_r)/(bottom)

cv.imshow('', ndvi)
cv.waitKey()
cv.destroyAllWindows()
