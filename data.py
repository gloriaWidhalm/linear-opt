import numpy as np

# Define the matrix A, vector b, and cost vector c
A = np.array([
    [-1, 1, 0, 2],
    [1, 0, 1, -3]
])
b = np.array([2, 1])
c = np.array([-1, 0, 0, 2])

# example 1
A1 = np.array([
    [1, -2, 1],
    [-1, 3, -2]
])
b1 = np.array([2, -3])
c1 = np.array([1, 3, 2])

# example 2
A2 = np.array([
    [2, 5, 1, 0, 3, 1],
    [0, 2, 2, -4, 2, -4],
    [3, 5, 1, 2, 6, 3]
])
b2 = np.array([9 / 4, 0, 4])
c2 = np.array([2, -4, 1, 4, 8, 4])


A3 = np.array([
    [1, -1, 2, -1, 0],
    [-2, 0, -1, 1, -1]
])
b3 = np.array([1, 1])
# c here not needed, so just set it to 0
c3 = np.array([1, -2, 0, 1, 3])

def get_data():
    return A3, b3, c3
