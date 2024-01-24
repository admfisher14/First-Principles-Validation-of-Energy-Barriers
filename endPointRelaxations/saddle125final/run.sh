#!/bin/bash
#SBATCH --ntasks-per-node=48
#SBATCH --time=12:00:00



module purge
module restore castep

cd /storage/eng/phrbwm/saddle125final

srun castep.mpi castep
