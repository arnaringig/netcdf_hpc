class Time:
    """
    This is a variable in a netCDF file.
    """

    def __init__(self, rootgrp):
        self.value = rootgrp.createVariable("time", "i", ("time",))
        self.value.units = "hours since 1900-01-01 00:00:00.0"
        self.value.long_name = "time"
        self.value.calendar = "gregorian"

    def populate(self, data):
        self.value[:] = data
