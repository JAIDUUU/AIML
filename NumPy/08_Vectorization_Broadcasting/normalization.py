# A quite common example of broadcasting in Vector Normalization. This is very
# common in machine learning and data preprocessing.
# Let’s take an example of Standard Vector Normalization i.e. transforming an array
# such that it has:
# • mean = 0
# • standard deviation = 1
# For each element xi in vector,
# Where:
# xinormalized = (xi − μ)/σ
# • μ = mean of the vector (or column)
# • σ = standard deviation

import numpy as np


arr=np.array([[1,2],[3,4]])
mean=np.mean(arr)
std_dev=np.std(arr)
normaized_arr=(arr-mean)/std_dev

print(normaized_arr)

arr1=np.array([[1,2],[3,4],[5,6]])
mean=np.mean(arr1,axis=0)
std_dev=np.std(arr1,axis=0)
print((arr1-mean)/std_dev)