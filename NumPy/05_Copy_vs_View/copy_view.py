import numpy as np 

# Copy v/s View
# • Views are fast and memory-efficient (no data duplication).
# • Copies are safe but slower and use more memory.

pt_list=[1,2,3,4,5]
copy_list=pt_list[1:5]
copy_list[1]=144

print(copy_list)
print(pt_list)

np_arrray=np.array([1,2,3,4,5])
view_array=np_arrray[1:5]
view_array[1]=144
print(view_array)
print(np_arrray)



copy_array=np_arrray[1:4].copy()
copy_array[2]=144
print(copy_array)
print(np_arrray)