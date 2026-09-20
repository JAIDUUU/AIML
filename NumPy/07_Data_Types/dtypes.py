# Data Types in NumPy
# We have already discussed how every NumPy array has a single data type
# (homogeneous arrays) & it is stored in the .dtype attribute.
# Now, let’s look into some of the most common data types in NumPy:
# • Integer literals : int32 , int64
# • Floating literals : float32 , float64
# • Boolean : bool
# 7• Complex numbers : complex64 , complex128
# • String : S (byte-str) & U (unicode-str)
# • Object : generic python objects – object

import numpy as np 

arr=np.array([1,2,3,4])
arr1=np.array([1.0,2.3,3.44])
arr2=np.array(["hello","bro","IM"])

print(arr,arr.dtype)
print(arr1,arr1.dtype)
print(arr2,arr2.dtype)

#complex number
arr3=np.array([2+8j])
arr4=np.array([1+1j])
print(arr3,arr3.dtype)
print(arr3+arr4)
print(arr3-arr4)


# object
arr5=np.array(["apple",32,3.2,{33,22,11}])
print(arr5,arr5.dtype)