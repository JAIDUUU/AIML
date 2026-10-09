import numpy as np

#/////////////////////////////////////////////////////////////////////////////////////
# qustion)1
# x=np.array([10, 20, 30, 40, 50])
# print(x[[2,4]])


# q2
# x=np.arange(0,100,10)
# print(x)

# q3
# x=np.linspace(0,1,20)
# print(x)

# q4
# x=np.zeros((5,5))
# print(x)

# q5
# x=np.eye(4,4)
# print(x)

# q6
# x=np.full((3,4),7)
# print(x)

# q7
# x=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(x.shape,x.size,x.ndim,x.dtype)

# q8
# x=np.random.rand(1000,20)
# x=x[:800]
# print(x.shape,x)

# q9
# Y = x[:, -5:]

# q10
# arr = np.array([1,2,3,4,5,6,7,8])
# print(arr[::2])

# q11
# arr=np.array([50,92,32,22,43,4,4,32,31,54,32,83,12,31,62,3])
# print(arr[arr>50])

# q12
# arr = np.array([3,8,2,9,4,7])
# print(arr[arr%2==0])

# q13
# p = np.array([0.2,0.7,0.51,0.1,0.95])
# print(p[p>0.5])

# q14
# age = np.array([12,18,25,16,31,14])
# print(age[age>=18])

# q15
# x=np.random.randint(1,100,(100,5))
# arr=x[[0,10,50,99]]
# print(arr)


# q16
# x=np.arange(12)
# print(x.reshape((3,4)))

# q17
# x=np.arange(24).reshape(2,3,4)
# print(x)

# q18
# image=np.arange(784).reshape(28,28)
# print(image)

# q19
# image=np.arange(784).reshape(28,28)
# x=image.flatten()
# print(x)

# q20
# shape=np.random.rand(100,28,28)
# first_image=shape[0]
# print(first_image)

# q21
# image=np.random.rand(100, 28, 28)
# print(image[10:20])


# q22
# image=np.random.randint(0,256,(224,224,3))
# red_channel=image[:,:,0]
# print(red_channel)

# q23
# image=np.random.randint(0,256,(224,224,3))
# print(image[:100,:100,:])

# q24
# arr = np.array([10,20,30,40,50])
# print(arr[[1,2,4]])

# q25
# arr = np.array([1,2,3,4,5,6])
# print(arr[(arr>=2 )& (arr<=5)])

# q26
# x=np.random.rand(5000,10)
# print(x[:,:5])

# q27
# x=np.random.rand(5000,10)
# print(x[1000:2000])

# q28
# arr = np.array([1,2,3,4,5])
# x=arr.copy()
# x[0]=999
# print("X:",x)
# print(arr)

# q29
# arr=np.array([1,2,3,4,5])
# arr[0]=999
# print(arr)

# q30
# arr=np.array([1,2,3,4])
# changed=arr.astype("float32")
# print(changed)

# q31
# arr=np.array([1,2,3,4],dtype="float32")
# print(arr.dtype)

# q32
# X = np.array([1.2,2.8,3.9])
# chnaged=X.astype("int32")
# print(chnaged)

# q33
# x=np.array([1,2,3,4,5])
# print(x.dtype,x.itemsize)

#q34
# x=np.random.rand(10000,30)
# print(x.size)

# q35
# arr = np.array([[1,2,3],[4,5,6]])
# print(arr.sum())

# Q36
# arr = np.array([[1,2,3],[4,5,6]])
# sum=np.sum(arr,axis=0)
# print(sum)

# q37
# arr = np.array([[1,2,3],[4,5,6]])
# sum=np.sum(arr,axis=1)
# print(sum)

# q38
# arr=np.random.rand(1000,20)
# mean=np.mean(arr,axis=0)
# print(mean)

# q39
# arr=np.random.randint(0,100,size=(1000,20))
# mean=np.mean(arr,axis=1)
# print(mean)
