import numpy as np

m1 = np.loadtxt ('matrix1.txt')
m2 = np.loadtxt ('matrix2.txt')

x = (np.dot(m1,m2))
print(x)



