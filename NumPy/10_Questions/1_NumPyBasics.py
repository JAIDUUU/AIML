# What is NumPy, and how is a NumPy array different from a Python list?
# Create 1D, 2D, and 3D arrays using np.array().
# Find the ndim, shape, size, dtype, and itemsize of an array.
# Create arrays using np.zeros(), np.ones(), and np.empty().
# Use np.arange() to create an array containing even numbers from 1 to 50.
# Use np.linspace() to generate 11 equally spaced values between 0 and 1.
# Create NumPy arrays using different data types such as int32, float64, and bool.
# Convert a Python list into a NumPy array and a NumPy array back into a Python list

import numpy as np

# 1)
# array size is much lower then list size , numpy operations is faster more then list beacuse the use c lanuage 

# 2)
# arr1D=np.array([1,2,3])
# arr2D=np.array([[1,2,3],[4,5,6]])
# arr3D=np.array([[[1,3,4],[2,3,4]],[[4,5,6],[7,8,5]]])
# print(arr1D)
# print(arr2D)
# print(arr3D)

# 3)
# print(arr1D.shape,arr1D.ndim,arr1D.itemsize,arr1D.dtype)

# 4)
# zeros=np.zeros(3)
# zeros1=np.zeros((3,2))
# print(zeros)
# print(zeros1)

# identity=np.ones(4)
# identity1=np.ones((3,3))
# print(identity)
# print(identity1)

# empty=np.empty(2)
# print(empty)

# 5)arr=np.arange(2,51,2)
# print(arr)
# arr=np.arange(2,51,2)
# print(arr)

# 6)
# arr=np.linspace(0,1,11)
# print(arr)

#7) 
# arrint=np.array([1,2,3,4,5])
# arrfloat=np.array([1.2,2.0,3.0,4.7,5.0])
# arrbool=np.array([True,False])
# print(arrbool.dtype,arrbool)
# print(arrfloat,arrfloat.dtype)
# print(arrint,arrint.dtype)

# 8)
# lst=[1,2,3,4,5]
# arr=np.array(lst)
# last2=arr.tolist()   # NumPy array → List 

# print(arr)
# print(last2)