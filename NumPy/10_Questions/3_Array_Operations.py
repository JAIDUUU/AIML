
# ##  Array Operations
# * Perform addition, subtraction, multiplication, and division between two arrays.
# * Calculate the square and cube of every element in an array.
# * Calculate sum, mean, median, min, max, and std of an array.
# * Calculate row-wise and column-wise sums using the `axis` parameter.
# * Sort an array using `np.sort()`.
# * Find the indices of the maximum and minimum values using `np.argmax()` and `np.argmin()`.
# * Find unique values in an array and count their frequencies.
# * Find the common elements between two NumPy arrays.

# ---

import numpy as np 

arr1=np.array([10,5,77,5,3, 20, 30])
arr2=np.array([ 2,1,8,7,55 ,4,  5])

#17) 
# print(arr1+arr2)
# print(arr1-arr2)
# print(arr1*arr2)
# print(arr1/arr2)

# 18)
# print(arr1**2,arr1**3)

# 19)
# print(np.sum(arr1),np.mean(arr1),np.median(arr1),np.min(arr1),np.max(arr1),np.std(arr1))


# 20)
# arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(np.sum(arr,axis=0))
# print(np.sum(arr,axis=1))

# 21)
# print(np.sort(arr1))

# 22)
# print(np.argmin(arr1))
# print(np.argmax(arr1))

# 23)
# value,count=np.unique(arr1,return_counts=True)
# print(value)
# print(count)

# 24)
# print(np.intersect1d(arr1,arr2))

