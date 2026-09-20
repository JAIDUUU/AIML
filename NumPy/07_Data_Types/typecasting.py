import numpy as np

# chaning data type 

arr=np.array([1,2,3,4,5],dtype="float64")
print(arr,arr.dtype)

new_array=arr.astype("int16")
print(new_array,new_array.dtype)


# Why does dtype matter?
# • Memory efficiency
# ◦ np.int8 uses 1 byte per element, np.int64 uses 8 bytes.
# • Performance
# ◦ Smaller types = faster computations.
# • Compatibility
# ◦ Images often use np.uint8
# ◦ ML libraries expect float32