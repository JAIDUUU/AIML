import numpy as np


arr=np.array([1,2,3,4,5,6])
print(arr.shape)

reshaped=arr.reshape((2,3))
print(reshaped,reshaped.shape)

flattened=arr.flatten()    # dor converts in 2d to 1d
print(flattened,flattened.shape)
