import numpy as np

m = np.array([[1, 3, 2, 1], [3, -1, 2, 1], [4, -2, 4, 2], [1, 0, 7, 3]])

b = np.array([[12], [6], [10], [19]])

# find the inverse of m
inv_m = np.linalg.inv(m)

x = np.dot(inv_m, b)

print(x)
