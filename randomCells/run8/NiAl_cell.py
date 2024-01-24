#!/usr/bin/env python
# coding: utf-8

# In[28]:


import ase.io.lammpsdata as io
from ase.visualize import view
import os
import numpy as np
import ase.io as ase
#import ase.io.castep as castep
import ase.calculators.castep as castep


# In[29]:


def symbol_change(atoms):
    for j in range(len(atoms)):
        if atoms.symbols[j] =='H':
            atoms.symbols[j]='Ni'
        else:
            atoms.symbols[j]='Al'
initial = "random.data"            
atoms = io.read_lammps_data(initial,style="atomic")


# In[30]:





# In[31]:


symbol_change(atoms)


# In[32]:


calc =castep.Castep()
atoms.calc=calc
calc.initialize()


# In[36]:


#castep.write_cell("NiAl.cell",atoms)


# In[ ]:




