class Wt:
    """
    Workable Temperature
    This is a variable in a netCDF file.
    """

    def __init__(self, rootgrp):
        self.value = rootgrp.createVariable(
            "wt", "i", ("time", "latitude", "longitude"))
        self.value.units = "Boolean"
        self.value.long_name = "workable temperature"

    def populate(self, data):
        self.value[:] = data
