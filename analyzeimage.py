import numpy as np
from PIL import Image

def analyzeimage(old_image):
	# analyze the image 'old_image' here
	# save the analyzed image to 'static/temp.jpg'
	# return the path of the new image file

	# ndvi = nir - rgb
	#	     ---------
	#	     nir + rgb

	img = np.array(Image.open(old_image))

	return img

print(analyzeimage('images/wallplants.jpg'))