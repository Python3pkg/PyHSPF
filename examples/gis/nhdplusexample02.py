# nhdplusexample02.py
#
# David J. Lampert (djlampert@gmail.com)
#
# Shows how to use the NHDPlusDelineator to delineate the watershed for a point
# within a HUC8. Assumes the NHDPlus Hydrography data exist already. This 
# example delineates the watershed for the location of the discontinued flow
# gage at Hunting Creek, MD.

import os

# pyhspf imports

from pyhspf.preprocessing import NHDPlusDelineator

# paths to the downloaded and extracted files from NHDPlus for the HUC8.
# these are provided with the distribution now, though they can be generated
# from the previous example.

output = 'data'

# paths to the different source files for the model data

VAAfile   = '{}/flowlineVAAs'.format(output)   # NHDPlus value added attributes
flowfile  = '{}/flowlines'.format(output)      # HUC8 flowline shapefile
cfile     = '{}/catchments'.format(output)     # HUC8 catchment shapefile
elevfile  = '{}/elevations.tif'.format(output) # NED raster file

# make sure the files are in the right place

if not os.path.isfile(VAAfile):

    print(('\nerror: file {} does not exist!'.format(VAAfile)))
    print('double-check that the path is correct\n')
    raise

if not os.path.isfile(flowfile + '.shp'):

    print(('\nerror: file {} does not exist!'.format(flowfile)))
    print('double-check that the path is correct\n')
    raise

if not os.path.isfile(cfile + '.shp'):

    print(('\nerror: file {} does not exist!'.format(cfile)))
    print('double-check that the path is correct\n')
    raise

if not os.path.isfile(elevfile):

    print(('\nerror: file {} does not exist!'.format(elevfile)))
    print('double-check that the path is correct\n')
    raise

# create an instance of the delineator and supply the path to the source files

delineator = NHDPlusDelineator(VAAfile, flowfile, cfile, elevfile)

# longitude, latitude of the point to delineate (the delineator looks for the
# closest flowline to this point)

longitude = -76.6056
latitude  =  38.5839

# location to place the output (put it inside the existing HUC8 directory)

gageoutput = '{}/01594670'.format(output)

# file name plot of the output

plot = '{}/hunting_watershed'.format(gageoutput)

# extracts the catchments and flowlines for the gage's watershed and merge
# the shapes together to make a boundary file

delineator.delineate_watershed(longitude, latitude, output = gageoutput,
                               plot = plot)
