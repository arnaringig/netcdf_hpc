import numpy as np


class Mavg_t2m:
    """
    This variable is not being used. 
    Was written for development.
    This is a variable in a netCDF file.
    """
    # scale_factor = 6.110256380701088E-4
    # offset = 269.55664791735677

    def __init__(self, rootgrp):
        self.value = rootgrp.createVariable(
            "mavg_t2m", "i", ("time", "latitude", "longitude"), fill_value=0)
        self.value.valid_range = [180, 333]
        self.value.missing_value = 0
        self.value.long_name = "monthly average t2m"
        self.value.units = "K"

    def populate(self, data):
        self.value[:] = data
