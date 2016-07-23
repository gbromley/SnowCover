import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.io as sio
import netCDF4
import os

snow_data = '/data/SnowCover/data/'
track_data = '/data/SnowCover/tracks/'

snow_files = os.listdir(snow_data)
