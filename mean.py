import numpy as np
d = np.array([[10,20,30],[40,50,60]])
print(np.mean(d))
print(np.mean(d,axis = 0))


import numpy as np
data = np.array([10, 20, 30, 40, 50])
median_value = np.median(data)
print("Median:", median_value)


import numpy as np
data = np.array([10, 20, 30, 40, 50])
std_value = np.std(data)
print("Standard Deviation:", std_value)


a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(np.dot(a,b))


A = np.array([[1, 2, 3],
              [4, 5, 6]])
transpose_A = A.T
print(transpose_A)