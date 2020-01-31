import numpy as np
import sys

matrix1 = sys.argv[1]
matrix2 = sys.argv[2]

m1 = np.loadtxt(matrix1)
m2 = np.loadtxt(matrix2)

x = (np.dot(m1,m2))
print(x)


