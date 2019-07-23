#This is a veggie checker
# need to specify location of some certificates for rasterio
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