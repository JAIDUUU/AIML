import numpy as np

# operation along 2d 

arr2D=np.array([[1,2,3],[4,5,6],[7,8,9]])

print(np.sum(arr2D))

sum_of_column=np.sum(arr2D,axis=0)
print(sum_of_column)

sum_of_row=np.sum(arr2D,axis=1)
print(sum_of_row)

print(arr2D[0:2,1:3])

#operation along 3d

arr3D=np.array([[[1,2,3],[4,5,6]],[[1,3,5],[2,4,6]]])
print(arr3D,arr3D.ndim)

#indexing
print(arr3D[0][1][2])
print(arr3D[1][0][2])

print(arr3D[:,:,0])
print(arr3D[:,0,:])


#manuplating data 
arr3D[0,0,0]=33
print(arr3D)