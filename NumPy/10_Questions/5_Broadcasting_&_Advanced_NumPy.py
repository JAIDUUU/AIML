# ##  Broadcasting & Advanced NumPy
# * What is broadcasting in NumPy? Demonstrate it with arrays of different shapes.
# * Add a vector to every row of a matrix using broadcasting.
# * Perform matrix multiplication using `np.dot()` and the `@` operator.
# * Find the transpose of a matrix.
# * Create an identity matrix, diagonal matrix, and random matrix.
# * Generate random integers using `np.random` and make the results reproducible using a random seed.
# * Create an array containing `NaN` values and identify them using `np.isnan()`.
# * Replace `NaN` values with zero or the mean of the available values.
# * Normalize a NumPy array using Min-Max normalization.
# * **Mini Challenge:** Create a 2D array containing student marks and calculate each student's total, average,
# highest subject mark, pass/fail status, and class average.

import numpy as np
# 31) broadcasting ka mtlbb hn numpy ka diffrent shape kei beech operation automaticly perform 
# krran bina manually array ko same shape mein convert karei 

# 32) 
# arr=np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])

# sqr_arr=arr**2
# arr1=np.array([3,1,12])
# print(sqr_arr+arr1)

# 33)
# arr1=np.array([1,2,3,4])
# arr2=np.array([2,3,4,1])
# print(np.dot(arr1,arr2))
# print(arr2@arr1)

#34)
# matrix =np.array([
#     [1,2,3],[4,5,6]
# ])
# transpose=matrix.T
# print(transpose)

# 35)
# print(np.eye(3))
# print(np.diag([10,20,30]))
# print(np.random.rand(3, 3))

# 36)
