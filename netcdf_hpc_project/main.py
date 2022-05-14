#!/usr/bin/python3
import netCDF4 as nc
import numpy as np
from utilities import *
from packages import *
import sys
import os
import socket

def main():
    host = socket.gethostname()
    idx = int(sys.argv[1])-1 # file index
  
    dfile = f'/scratch/hpc_2022/arnar/repository/year_{idx}.nc'
    in_file_dataset = nc.Dataset(dfile)
    u10 = np.array(in_file_dataset['u10'][:])
    v10 = np.array(in_file_dataset['v10'][:])
    t2m = np.array(in_file_dataset['t2m'][:])
    tp = np.array(in_file_dataset['tp'][:])

    # workable wind magnitude
    wwm_data = Calculations.calculate_wwm(u10, v10)
    # workable temperature
    wt_data = Calculations.calculate_wt(t2m)
    # workable precipitation
    wp_data = Calculations.calculate_wp(tp)
    # Logical AND from the three variables we have just calculated
    summary_data = Calculations.calculate_summary(wwm_data, wt_data, wp_data)

    of_builder = OutfileBuilder(in_file_dataset, idx)
    of_builder.populate_georeferenced_variables(
        wwm_data, wt_data, wp_data, summary_data)

    print(f"Process at {host} ({str(os.cpu_count())} cpu-s) is complete")



main()
