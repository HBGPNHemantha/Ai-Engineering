import numpy as np

arr=np.array([1,2,3,4,5,6])
#print(arr)
zeroes = np.zeros((3,3))
#print(zeroes)

ones=np.ones((2,4))
#print(ones)

#range_arr=np.arange(1,10)
range_arr=np.arange(1,10,2)
#print(range_arr)

#linspace_arr=np.linspace(0,10,5)
linspace_arr=np.linspace(0,10,3)
#print(linspace_arr)

reshaped = arr.reshape(3,2)
#print(reshaped)

expanded = arr[:,np.newaxis]
#print(expanded)

a=np.array([1,2,3])
b=np.array([4,5,6])
#print(a+b)
#print(a*b)
#print(a/b)
c=np.array([4,9,25])
#print(np.sqrt(c))
#print(np.max(c))
#print(np.mean(c))

d = np.array([10,20,30,40,50,60])
print(d[2])
print(d[-1])
print(d[1:4])
print(d[:3])
print(d[3:])

reshape=d.reshape(2,3)
print(reshape)
