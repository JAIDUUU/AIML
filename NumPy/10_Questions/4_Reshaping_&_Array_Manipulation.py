
# ## Reshaping & Array Manipulation
# * Reshape a 1D array into 2D and 3D arrays.
# * Explain and demonstrate the difference between `reshape()` and `resize()`.
# * Flatten an array using both `flatten()` and `ravel()`.
# * Combine two arrays vertically and horizontally.
# * Use `np.concatenate()`, `np.vstack()`, and `np.hstack()`.
# * Split an array into multiple smaller arrays using `np.split()`.


import numpy as np 

arr1D=np.array([1,2,3,4,8,4,5,5,6])
arr2Da=np.array([[6,4,8],[3,1,0]])
arr2Db=np.array([[1,2,8],[4,5,6]])
# arr3D=np.array([[[1,3,4],[2,3,4]],[[4,5,6],[7,8,5]]])

# 25)
# resape=arr1D.reshape(2,2)
# print(resape)

# arr3D=arr1D.reshape(2,1,3)
# print(arr3D)

# 26)
# resape=arr1D.reshape(3,3)
# resizee=arr1D.resize(3,3)
# print(arr1D)

# reshape() → new shape deta hai, original array change nahi hota.
# resize() → original array ko directly change karta hai.

# 27)
# use=arr2D.flatten()
# print(use)
# # flatten() → copy banata hai
# # ravel() → generally view deta hai
# AVEL=arr2D.ravel()

# 28)
# print(np.vstack((arr2Da,arr2Db)))
# print(np.hstack((arr2Db,arr2Da)))

# 29)
# axis=0 → upar-neeche (vertical)
# axis=1 → left-right (horizontal)


#print(np.concatenate((arr2Da, arr2Db), axis=1))   # for combine 
# print(np.vstack((arr2Da,arr2Db)))
# print(np.hstack((arr2Db,arr2Da)))

# 30)
print(np.split(arr1D,3))