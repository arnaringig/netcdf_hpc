import netCDF4 as nc
import numpy as np
from utilities import *
from ..variables import *


class OutfileBuilder:
    """ 
    NetCDF Outfile Builder
    We will create identical variables in the new netCDF file
    identical to the ones in the input file
    The dimensions dim come from the input file
    """

    def __init__(self, infile, idx):

        self.infile = infile
        self.infile_dim = infile.dimensions
        self.rootgrp = nc.Dataset(
            f"./output/outfiles/outfile_year_{idx}.nc", "w", format="NETCDF4")
        self.__initialize_dimensions()
        ####
        # Initialize variables for outfile:
        #
        # Base variables:
        self.latitude = Latitude(self.rootgrp)
        self.longitude = Longitude(self.rootgrp)
        self.time = Time(self.rootgrp)
        # Georeferenced variables:
        self.wwm = Wwm(self.rootgrp)
        self.wt = Wt(self.rootgrp)
        self.wp = Wp(self.rootgrp)
        self.summary = Summary(self.rootgrp)
        ####
        self.__initialize_base_variables()

    def __create_dimension(self, name, size):
        self.rootgrp.createDimension(name, size)

    def __initialize_dimensions(self):
        self.__create_dimension(
            self.infile_dim['latitude'].name, self.infile_dim['latitude'].size)
        self.__create_dimension(
            self.infile_dim['longitude'].name, self.infile_dim['longitude'].size)
        self.__create_dimension(
            self.infile_dim['time'].name, self.infile_dim['time'].size)

    def __initialize_base_variables(self):
        self.latitude.populate(np.array(self.infile['latitude']))
        self.longitude.populate(np.array(self.infile['longitude']))
        self.time.populate(np.array(np.array(self.infile['time'])))

    def populate_georeferenced_variables(self, wwm_data, wt_data, wp_data, summary_data):
        self.wwm.populate(wwm_data)
        self.wt.populate(wt_data)
        self.wp.populate(wp_data)
        self.summary.populate(summary_data)
