class Latitude:
    """
    This is a variable in a netCDF file.
    """

    def __init__(self, rootgrp):
        self.value = rootgrp.createVariable("latitude", "f", ("latitude",))
        self.value.units = "degrees_north"
        self.value.long_name = "latitude"

    def populate(self, data):
        self.value[:] = data
