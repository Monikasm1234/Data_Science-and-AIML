import numpy as np
readings = np.arange(24)
reshaped = readings.reshape(4, 3, 2)
transposed = reshaped.transpose(0, 2, 1)
print("Final Shape:", transposed.shape)
print("Final Array:\n", transposed)