class Summary:
    """
    Workable Precipitation
    This is a variable in a netCDF file.
    """

    def __init__(self, rootgrp):
        self.value = rootgrp.createVariable(
            "summary", "i", ("time", "latitude", "longitude"))
        self.value.units = "Boolean"
        self.value.long_name = "logical AND of wwm, wt and wp"

    def populate(self, data):
        self.value[:] = data
