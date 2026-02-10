import numpy as np

#Array Initialization Methods- creating an array by giving starting no, end no and the increment
# Using arange (Start, Stop, Step)
arr = np.arange(40, 55, 3)
print("Array of numbers:", arr)
#two dimensional array
print(arr.shape)
arr_1 =np.arange(1,17).reshape(4,4)
print(arr_1)

#np.linspace(start, stop, num)- ---syntax(num-no of values)

#NumPy calculates the step size automatically. 
# Step size=(stop−start​) / num-1

# Using linspace (Evenly spaced)
arr = np.linspace(0, 2, 5)
print(arr)

# Random values
arr = np.random.rand(2, 2)
print(arr)
#rand() → Only floats in [0, 1)-generates a 2×2 array (matrix) 
# filled with random numbers between 0 and 1.