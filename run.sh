#!/bin/bash
#
#SBATCH --job-name=myJobarrayTest
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --array=1-10
#SBATCH --output=output/python_log/python_output_%A_%a.out
#SBATCH --error=output/err/errorlog_%A_%a.err
srun python3 /scratch/hpc_2022/arnar/netcdf_hpc_project/main.py $SLURM_ARRAY_TASK_ID