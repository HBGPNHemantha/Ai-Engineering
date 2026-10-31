import numpy as np
mat=np.array([[1,2,3],[2,3,4],[5,6,7]])
vector=np.array([1,0,-1])
result_add = mat+vector
print("add:\n",result_add)

result_mul = mat*2
print("mul:\n",result_mul)

#generate random dataset
data=np.random.randint(1,51,size=(5,5))
print("random dataset:\n",data)

#filter val
data[data>25]=0
print("modified dataset:\n",data)

#calculate the summary
print("sum: ",np.sum(data))
print("mean: ",np.mean(data))
print("std: ",np.std(data))