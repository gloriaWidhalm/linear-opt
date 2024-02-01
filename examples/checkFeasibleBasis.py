# Define the matrix A and vector b from the LP
A = np.array([
    [1, 1, 1, 0, 0],
    [2, 1, 0, 1, 0],
    [-1, 1, 0, 0, 1]
])

b = np.array([6, 10, 4])

# Basis B corresponds to the columns for x3, x4, x5 (the last three columns of A)
B = [2, 3, 4]  # Using zero-based indexing for Python

# x1 = np.array([2, -1, 2, 0, 1, 0, 0])
# x2 = np.array([1, 0, 1, 0, 1, 0, 0])
# x3 = np.array([0, 0, 1, 1, 0, 0, 0])
# x4 = np.array([0, 0.5, 0, 0, 0.5, 0, 1])
#
# check_feasible_basis(A, x1, b)
# check_feasible_basis(A, x2, b)
# check_feasible_basis(A, x3, b)
# check_feasible_basis(A, x4, b)