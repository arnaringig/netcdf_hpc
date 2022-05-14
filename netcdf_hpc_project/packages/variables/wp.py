class Wp:
    """
    Workable Precipitation
    This is a variable in a netCDF file.
    """

    def __init__(self, rootgrp):
        self.value = rootgrp.createVariable(
            "wp", "i", ("time", "latitude", "longitude"))
        self.value.units = "Boolean"
        self.value.long_name = "workable precipitation"

    def populate(self, data):
        self.value[:] = data
