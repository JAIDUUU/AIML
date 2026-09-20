import numpy as np


arr=np.array([[1,2,3],[4,5,6],[7,8,9]])

print(arr.shape) #dimenstions
print(arr.size)  #total elemnts
print(arr.ndim)  #number of dimenstions
print(arr.dtype)  #data type 
print(arr.itemsize) # size of each elements


#explicity chaneges 

str_arr=np.array([1,2,3],dtype="U")
print(str_arr,str_arr.dtype)

float_arr=np.array([1,2,3],dtype="float64")
print(float_arr,float_arr.dtype)

int_arr = float_arr.astype(np.int64)
print(int_arr, int_arr.dtype)