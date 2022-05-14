class Longitude:
    """
    This is a variable in a netCDF file.
    """

    def __init__(self, rootgrp):
        self.value = rootgrp.createVariable("longitude", "f", ("longitude",))
        self.value.units = "degrees_east"
        self.value.long_name = "longitude"

    def populate(self, data):
        self.value[:] = data
