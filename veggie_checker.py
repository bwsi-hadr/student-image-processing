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
<<<<<<< HEAD
import matplotlib.pyplot as plt
#dylan tf u so gay for though
=======
import matplotlib.pyplot as plt
>>>>>>> ec3a47e071b5d7f08b9b68d1684a5af2677d64a1
