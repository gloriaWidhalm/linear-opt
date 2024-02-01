import numpy as np

from findCanonicalForm import print_problem_information, get_canonical_form

z=0
# define numpy array matrix A
A = np.array([
    [1, -2, 1, 1, 0],
    [1, -3, 2, 0, 1]
])
# define b as a numpy vector, constraints b
b = np.array([2, 3])
# define c as a numpy vector, objective function c
c = np.array([0, 0, 0, 1, 1])

# Define which variables are in the (new) basis
# Finding the canonical form
B = np.array([3, 4])

print_problem_information(A, b, c, z, B)
# get canonical form
A, b, c, z = get_canonical_form(A, b, c, z, B)
print("----- Solution -----")
# canonical form for new basis
print_problem_information(A, b, c, z)

print("--------------------------")

# Use new basis and get new canonical form
B = np.array([2, 3])
print("new basis: ", B)
print_problem_information(A, b, c, z, B)
# get canonical form
A, b, c, z = get_canonical_form(A, b, c, z, B)
print("----- Solution -----")
# canonical form for new basis
print_problem_information(A, b, c, z)
print("--------------------------")

# Use new basis and get new canonical form
B = np.array([0, 2])
print("new basis: ", B)
print_problem_information(A, b, c, z, B)
# get canonical form
A, b, c, z = get_canonical_form(A, b, c, z, B)
print("----- Solution -----")
# canonical form for new basis
print_problem_information(A, b, c, z)
print("--------------------------")