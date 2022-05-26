import numpy as np
import control
import control.matlab
import longitudinal as long
import latdir
from trim import TrimState
from data import get_aircraft_data

data_list = get_aircraft_data()
for data_dict in data_list: globals().update(data_dict)

# trim

# LONGITUDINAL: 

# get A matrix
Along = long.get_A_long()

# get B matrix
Blong = long.get_B_long

# eigenvalues
long_eigs, _ = np.linalg.eig(Along)

# Damp coef. and wn

# Response over time

# LATDIR
# get A matrix
Alatdir = latdir.get_A_lat()

# get B matrix
Blatdir = latdir.get_B_lat()

# eigenvalues
latdir_eigs, _ = np.linalg.eig(Along)

# Damp coef. and wn


# Response over time


