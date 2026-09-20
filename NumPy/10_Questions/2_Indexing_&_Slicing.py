# * Access the first, last, and middle elements of a 1D array.
# * Access a specific row and column from a 2D array.
# * Extract the first two rows and last two columns from a 2D array.
# * Reverse a NumPy array using slicing.
# * Access a specific element from a 3D array.
# * Use Boolean indexing to extract all values greater than 50.
# * Extract all even and odd numbers from an array.
# * Replace elements in an array that satisfy a given condition.

import numpy as np

arr1D=np.array([1,2,3,4,5])
arr2D=np.array([[1,2,3],[4,5,6]])
arr3D=np.array([[[1,3,4],[2,3,4]],[[4,5,6],[7,8,5]]])

# 9)
# print(arr1D[0])
# print(arr1D[-1])
# print(arr1D[len(arr1D)//2])

# 10)
# print(arr2D[1])
# print(arr2D[:,1])

#11)

# print(arr2D[:2])
# print(arr2D[-2:])

# 12)
# print(arr1D[::-1])

# 13)
# print(arr3D[0,1,2])

# 14)
# arr=np.array([10, 25, 60, 75, 40, 90])
# print(arr[arr>50])

# 15)
# arr1=np.arange(0,51)
# even_arr=arr1[arr1%2==0]
# odd_arr=arr1[arr1%2!=0]
# print(even_arr,odd_arr)

# 16)
# arr3=np.array([10,20,30,40,50])
# arr3[arr3>30]=0
# print(arr3)