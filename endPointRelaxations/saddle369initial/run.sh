#!/bin/bash
#SBATCH --ntasks-per-node=48
#SBATCH --time=12:00:00



module purge
module restore castep

cd /storage/eng/phrbwm/saddle369initial

srun castep.mpi castep
