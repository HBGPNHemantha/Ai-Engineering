import numpy as np
a=np.arange(1,4)
b=np.arange(5,8)
print("original a: ",a)
print("original b: ",b)
print(f"add: {a+b}")
print(f"sub: {a-b}")
print(f"mul: {a*b}")
print(f"div: {a/b}")

mat = np.arange(1,10)
matrix=mat.reshape(3,3)
transpose=matrix.T
print("array: ",mat)
print("matrix: ",matrix)
print("Transpose: ",transpose)
mat2=np.arange(11,20)
matrix2=mat2.reshape(3,3)

print(f"add:\n {matrix+matrix2}")
print(f"sub:\n {matrix-matrix2}")
print(f"mul:\n {matrix*matrix2}")