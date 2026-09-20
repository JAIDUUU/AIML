# Multi-dimensional arrays in NumPy are the foundation of most scientific and
# machine-learning work.
# A NumPy array can have any number of dimensions (1D, 2D, 3D & so on). Each
# dimension is called an axis.
# • 1D array has 1 axis (axis0).
# • 2D array has 2 axes (axis0 = rows, axis1 = columns)
# • 3D array has 3 axes (axis0 = depth/layer, axis1 = rows in each layer, axis2 =
# columns in each layer)

import numpy as np 


arr1D=np.array([2,4,5])
print(arr1D,arr1D.ndim)