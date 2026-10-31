import numpy as np
#array and scaler broadcasting
#arr=np.array([1,2,3,4,5,6])
#print(arr +10)

#matrix=np.array([[1,2,3],[4,5,6]])
#vector=np.array([1,0,1])

#print(matrix +vector)

#aggretion function

#print("sum: ",np.sum(matrix))
#print("mean: ",np.mean(matrix))
#print("max: ",np.max(matrix))
#print("standard deviation: ",np.std(matrix))
#print("sum along rows: ",np.sum(matrix,axis=1))
#print("sum along columns: ",np.sum(matrix,axis=0))


#boolean indexing
#evens = arr[arr % 2 == 0]
#print("evens: ",evens)
#arr[arr>3]=0
#print("modified array: ",arr)

#seting random seed
#np.random.seed(42) #hamaweleema ekama random set eka denne
#random number generation

random_arr=np.random.rand(3,3)
print("random array: \n",random_arr)
random_int=np.random.randint(0,100,size=(2,3))
print("random integer: \n",random_int)

#seting random seed
np.random.seed(42) #hamaweleema ekama random set eka denne