import numpy as np
mat1=([[1,2,3],[4,5,6],[6,7,8]])
mat2=([[4,3,2],[2,1,3],[1,1,2]])
print("ADDITION")
print(np.add(mat1,mat2))
print("SUBTRACTION")
print(np.subtract(mat1,mat2))
print("DIVISION")
print(np.divide(mat1,mat2))
print("MULTIPLY")
print(np.multiply(mat1,mat2))

from numpy import array
from scipy.linalg import svd
a=array([[1,2,3],[4,5,6],[1,2,2]])
U,s,VT=svd(a)
print("\nDecomposed matrix \n",U)
print("\nInverse matrix \n",s)
print("\nTranspose matrix \n",VT)

