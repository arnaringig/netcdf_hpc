### To fetch the data 

If you are interested in learning how to use the Copernicus API and use the api included in this project to fetch the data please follow the link below:

#### [How to use the Copernicus API](https://cds.climate.copernicus.eu/api-how-to)

Alternatively, if you just want to download the data fast and get running:
[Download the data from this Google Drive folder](https://drive.google.com/drive/folders/1XSq_dOUmYSJ8f2edBzYdFGVLLtQeG6sB?usp=sharing) directly and put it into the */repository* folder in the project root, with the project residing on your local machine.

The packages *numpy*, *netCDF4* and *cdsapi*(*) must be available to python on the remote host. They can be installed using the [pip](https://pip.pypa.io/en/stable/) package manager as follows (contact your HPC administrator if you don´t have privileges to pip install):

(*) The cdsapi only needs to be available if you intend to use the Copernicus API to fetch data.

```bash
pip install numpy netCDF4 cdsapi
```

### To upload from your local machine to the remote host

```shell
$ scp -r /path/to/local/source user@ssh.example.com:/path/to/remote/destination 
```
### To run the project on the remote host
```shell
$ sbatch run.sh 
```
This will execute the following shell script:
 Make sure to update the path to your folder in the run.sh file
```shell
#!/bin/bash
#
#SBATCH --job-name=myJobarrayTest
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --array=1-10
#SBATCH --output=output/python_log/python_output_%A_%a.out
#SBATCH --error=output/err/errorlog_%A_%a.err
srun python3 /path/to/your/folder/netcdf_hpc_project/main.py $SLURM_ARRAY_TASK_ID 
```

## Output:

If the project is run correctly, the output files will be placed in the */output/outfiles* folder in the project root. A print statement from Python for each node will be available in */output/python_log* for each successful process. Error logs will be available in */output/err*.



### To visualize the data being processed visit the following vimeo link:
# [watch video](https://vimeo.com/709715414)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)