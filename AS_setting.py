import numpy as np

# first  part simulation
# ATS probability matrix and adapting steps for Ciw
routing_AM_TO_SCE_raw = np.array(
    [[0, 0, 0, 0, 0.028,	0,	0.028,	0.028,	0,	0,	0,	0.028,	0.028,	0,	0,	0.085,	0,	0.028,	0,	0,	0,	0,	0.028,	0,	0.028,	0,	0,	0,	0.028,	0,	0.028,	0,	0,	0,	0.171,	0,	0,	0,	0.028,	0,	0,	0,	0.057,	0,	0,	0.085,	0,	0.028,	0.2, 0,	0,	0,	0,	0.028,	0.028,	0],
     [0, 0, 0, 0,	0,	0,	0,	0.027,	0,	0.027,	0.027,	0,	0.027,	0.027,	0.083,	0.027,	0.027,	0.027,	0.043,	0.027,	0,	0,	0.027,	0.027,	0,	0.027,	0,	0,	0,	0,	0,	0.027,	0,	0,	0.027,	0,	0.027,	0,	0.027,	0,	0,	0,	0,	0.027,	0,	0.111,	0.027,	0,	0.055,	0,	0.055,	0,	0,	0.083,	0.083,	0],
     [0, 0, 0, 0.007,	0,	0.007,	0,	0,	0.007,	0.023,	0.046,	0,	0.046,	0.1, 0,	0.007,	0,	0,	0,	0.007,	0.007,	0.007,	0.023,	0.023,	0,	0,	0.015,	0.015,	0,	0.007,	0.007,	0.007,	0.007,	0.046,	0.038,	0.007,	0.007,	0.007,	0,	0.015,	0.007,	0.015,	0.007,	0,	0.007,	0.238,	0.007,	0,	0.046,	0.092,	0.03,	0.015,	0.007,	0.007,	0,	0.015]]
)

routing_AM_TO_SCE = np.concatenate((routing_AM_TO_SCE_raw, np.zeros((53, 56))), axis=0).tolist()

# scene places simulation time and adapting steps for Ciw
scene_time_raw = np.array([1.33, 0.4, 1.71, 0.63, 1.64, 0.57, 1.55, 1.05, 2, 1.86, 1.07, 1.2, 0.78, 6, 0.36, 0.7, 0.44, 0.86, 0.29, 1.06, 1.43, 0.19, 0.8, 0.51, 0.58, 2, 2, 1.38, 1.45, 0.67, 0.37, 1.94, 1.71, 0.24, 1.33, 0.15, 0.46, 0.74, 0.41, 0.67, 0.4, 2.40, 0.54, 0.95, 1, 1.40, 0.49, 0.82, 0.52, 0.29, 1.96, 2.47, 2.55])

ATS_time_raw = []
for i in scene_time_raw:
 j = 1/i
 ATS_time_raw.append(j)

ATS_time = [0, 0, 0] + ATS_time_raw

# scene places capability
SCE_capability = [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1]


# second part simulation, carry patient to destination

# curing time in every scene place as the arrival time
emer_time_raw = [0.8, 2, 0.42, 2, 3, 1, 1.03, 0.99, 1, 2.00, 0.96, 0.90, 1.56, 1.5, 1.5, 4.8, 4, 3.33, 0.8, 1.42, 2, 1.2, 2, 1, 1.01, 3, 2.73, 0.73, 2.07, 2.61, 0.69, 1.21, 3, 0.64, 6, 1.5, 2.33, 1.94, 0.66, 1.26, 6, 0.92, 1.14, 0.34, 2, 1.71, 1.04, 1, 0.57, 0.29, 1.63, 2.30, 1.29]

# the simulation time of ambulances arriving in every destination
des_time_raw = [0.09, 0.94, 2, 1.13, 0.44, 0.52, 3.64, 0.8, 0.18, 0.78, 0.41, 0.95, 2.22, 1.76, 0.54, 0.67, 1.85, 1.2, 2, 3, 2, 4, 2, 1.40, 3, 3.83, 2.18, 1.28, 1.12, 0.63, 1.74, 0.39, 1.42, 1, 0.85, 1.84, 1.71, 1.33, 1.43, 1.84, 2.25, 0.69, 0.73, 1.70, 1.03, 0.53, 2.4, 4, 1.47, 2.4, 0.86, 0.8, 3, 2.36]

# adapting to Ciw
emer_time = emer_time_raw + [0 for i in range(len(des_time_raw))]
des_time = [0 for i in range(len(emer_time_raw))] + des_time_raw

# STD probability matrix
routing_SCE_TO_DES_raw = np.array(
    [[0,  0, 0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,  0, 1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0, 0, 0, 0,	0, 0, 	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0, 0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0, 0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0, 0,	0,	0,	0,	0,	0.5,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.5,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0, 0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0, 0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.25,	0,	0,	0,	0.25,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.5,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0.142,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.285,	0,	0,	0,	0.142,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.142,	0,	0,	0,	0,	0,	0,	0.142,	0,	0,	0,	0,	0.142,	0,	0,	0,	0],
     [0, 0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.5,	0,	0,	0,	0.125,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.125,	0,	0,	0,	0.125,	0.125,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.142,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.071,	0,	0.071,	0,	0,	0,	0.071,	0,	0,	0,	0,	0,	0,	0,	0.071,	0,	0.071,	0,	0.142,	0,	0,	0,	0.142,	0,	0,	0,	0,	0.214],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.666,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.333,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0.2,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.2,	0,	0,	0,	0,	0,	0,	0.2,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.4,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.5,	0,	0,	0,	0,	0,	0,	0.5,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.5,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.5,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0.5,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.5,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0, 0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.2,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.2,	0,	0,	0.2,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.2,	0,	0,	0,	0.2, 0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.25,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.25,	0,	0,	0,	0,	0,	0.5,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.5,	0,	0,	0.5,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.5,	0,	0,	0,	0,	0,	0,	0.5,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.5,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.5,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.333,	0.333,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.166,	0,	0,	0,	0, 0,	0,	0,	0,	0,	0,	0,	0,	0,	0.166],
     [0,	0,	0,	0.083,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.083,	0,	0,	0.083,	0,	0,	0,	0,	0.166,	0,	0.083,	0.083,	0,	0,	0,	0,	0,	0,	0.083,	0,	0,	0,	0,	0,	0,	0,	0,	0.25,	0,	0,	0,	0,	0,	0,	0,	0,	0.083],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0.5,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.5,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.5,	0,	0.5,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0.5,	0.5,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.333,	0,	0,	0,	0,	0,	0,	0,	0.333,	0,	0,	0,	0,	0,	0.333,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0.026,	0,	0,	0,	0,	0,	0,	0.026,	0,	0.026,	0,	0,	0,	0,	0,	0, 0,	0,	0,	0,	0,	0,	0,	0.394,	0,	0,	0,	0,	0,	0.026,	0.263,	0,	0,	0,	0,	0.026,	0,	0,	0,	0.131,	0,	0,	0,	0.052,	0,	0,	0,	0,	0.026],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.5,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.5,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0.066,	0,	0,	0,	0,	0,	0.066,	0,	0,	0.066,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.066,	0,	0,	0,	0.066,	0,	0,	0,	0.066,	0,	0,	0.2,	0,	0.2,	0,	0,	0,	0.066,	0,	0,	0.066,	0.066,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.083,	0,	0,	0,	0.083,	0,	0,	0,	0,	0,	0,	0,	0,	0.416,	0,	0,	0.083,	0.083,	0.083,	0.083,	0,	0,	0,	0,	0,	0.083],
     [0,	0,	0,	0,	0.166,	0,	0,	0,	0,	0,	0,	0,	0.166,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.166,	0,	0,	0,	0,	0,	0.166,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.166,	0,	0,	0,	0.166,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.5,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.5,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.2,	0.6,	0,	0,	0,	0,	0,	0,	0,	0.2,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.25,	0,	0,	0,	0.25,	0.25,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.25,	0,	0,	0,	0,	0],
     [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1]
]
)

# adapting to Ciw
STD_raw_1 = np.concatenate((np.zeros((53, 53)), routing_SCE_TO_DES_raw), axis=1)

STD_metrix = np.concatenate((np.zeros((len(des_time_raw), len(STD_raw_1[0]))), STD_raw_1), axis=0).tolist()

# the num of hospital in every destination
hospital_setting = [1, 17, 17, 18, 15, 18, 12, 17, 15, 18, 17, 17, 19, 17, 20, 16, 18, 20, 13, 12, 18, 14, 18, 15, 22, 18, 19, 11, 18, 15, 15, 19, 13, 14, 12, 17, 14, 11, 11, 20, 13, 13, 16, 19, 18, 11, 17, 17, 15, 16, 15, 13, 15, 9]

# optimization method
SCE_capability[9] += 1
SCE_capability[50] += 3



