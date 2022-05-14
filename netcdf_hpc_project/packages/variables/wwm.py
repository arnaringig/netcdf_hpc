class Wwm:
    """
    Workable Wind Magnitude
    This is a variable in a netCDF file.
    """

    def __init__(self, rootgrp):
        self.value = rootgrp.createVariable(
            "wwm", "i", ("time", "latitude", "longitude"))
        self.value.units = "Boolean"
        self.value.long_name = "workable wind magnitude"

    def populate(self, data):
        self.value[:] = data
