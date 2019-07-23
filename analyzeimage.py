

def analyzeimage(old_image):
	# analyze the image 'old_image' here
	# save the analyzed image to 'static/temp.jpg'
	# return the path of the new image file
	!export CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
	try:
	import rasterio
	import rasterio.plot
	except:
	!pip install rasterio
	import rasterio
	import rasterio.plot

	try:
	import pyproj
	except:
	!pip install pyproj
	import pyproj

	import gdal
	import numpy as np
	import matplotlib
	import matplotlib.pyplot as plt
	return "static/temp.jpg"