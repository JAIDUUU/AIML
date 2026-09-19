import numpy as np
import time
import sys

# performance Comparision 
size= 10_000_000

#python list 
pythonList=list(range(size))
start=time.time()

list_squared=[x**2 for x in pythonList]
end=time.time()
print(f"python list timing: {end-start}sec")


#numapy arrray 
np_array=np.array(pythonList)
start=time.time()

array_squared=np_array**2 #vectorized operation 
end=time.time()
print(f"array time: {end-start}sec")



#memory usage Comparison
print("python list size:",sys.getsizeof(pythonList)*len(pythonList))
print("Numpay array size",np_array.nbytes)