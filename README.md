# First-Principles-Validation-of-Energy-Barriers

Required software:

Lammps with replica, KIM packages installed (https://www.lammps.org/#gsc.tab=0)

CASTEP (http://www.castep.org/)

KIM API (https://openkim.org/)

Python 


#barriers 

This contains the outfiles for the castep neb runs for the barriers used in the paper

#endPointRelaxations

This folder contains the end points of the castep neb which have to be relaxed before performing the neb

#randomCells

This contains the files used to calculated the lattice parameter used for all castep calculations

#Energies.dat

This files contains the data on the kMC ran to find the 500 barriers

#allconf_defect

This files contains all the configurations from the kMC 

#Cellcutting.ipynb 

Takes the file allconf_defect and splits it into individual configurations and saves them.
It then takes these files and cuts down to smaller cells so to be small enough to run CASTEP NEB on them.
The files are then saved.

#Flicker_finder.ipynb

Finds the end of flicker in the kMC simulations. This is when an atom first moves from it's initial position in one step, returns to the initial position in the next step and then moves to a different position in the next step.

#Geom_file_reader.ipynb

This file reads outputs found in #endPointRelaxations and writes the input files for the CASTEP NEB

#Lammps_file_builder.ipynb

stateRelax : Takes a KIMID and a cut down cell file from ##Cellcutting.ipynb and writes a lammps file to relax the end points based on that potential

nebFile : Writes the file that tells lammps where the atoms end upat the end point of the neb. Requires stateRelax to have been ran to get a relaxed endpoint

nebExcuteable : Writes a lammps neb input file for a given start and end point. Both need to have been relaxed using stateRelax and the end point needs to have been ran using nebFile

All files output form these functions will be needed to run Lammps neb

#CASTEP_NEB_READ.ipynb 

This note book will read the output files of a CASTEP NEB and save the barrier(s) into a numpy array for further analysis

#Vibrations.ipynb

This note book calculates prefactors for events 

#Vibrations.zip

This contains all the vibrational frequency data used for prefactors


