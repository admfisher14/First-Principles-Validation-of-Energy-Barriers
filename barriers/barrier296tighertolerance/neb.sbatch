#!/bin/bash
#SBATCH --nodes=5
#SBATCH --ntasks-per-node=48

#SBATCH --time=24:00:00


module purge
module load iccifort/2020.4.304  impi/2019.9.304 imkl/2020.4.304

srun  ../castep-castep-b807d1bba19f/obj/linux_x86_64_ifort--mpi/castep.mpi neb 
