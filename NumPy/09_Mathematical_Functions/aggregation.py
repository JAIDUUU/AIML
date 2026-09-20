# Useful Mathematical Functions
# NumPy is massive & provides a wide range of built-in mathematical functions that
# are highly optimized and can operate element-wise on arrays. Let’s have a look at
# some of them:
# Aggregation Functions
# These are functions that take an array and reduce it to a single value (or smaller array)
# by combining elements.
# 1.sum()- returns sum of all elements
# 2.prod()- returns product of all elements
# 3.min()- returns minimum value
# 4.max()- returns maximum value
# 5.argmin()
# - returns index of min value
# 6.argmax()
# - returns index of max value
# 7.mean()8.median()
# 9.std()
# - returns mean (average)
# - returns median
# - returns standard deviation
# 10. var() - returns variance

import numpy as np 

arr=np.array([1,2,3,4,5])
print(np.sum(arr))
print(np.prod(arr))
print(np.min(arr))
print(np.max(arr))
print(np.argmax(arr))
print(np.argmin(arr))
print(np.min(arr))
print(np.std(arr))
print(np.var(arr))
