import numpy as np

a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("2nd element of 1st row :", a[0,1])  #a[row,colum]

a = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[1,2,3,6]]])
print(a[0,1,3])  #a[axis,row,column]

a = np.array([1,2,3,4,5,6,7])
print(a[1:5])