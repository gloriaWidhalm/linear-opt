# write a function that checks if a given solution is unbounded

import numpy as np


def check_unbounded(A, b, x, d):
    """
    Check if the problem is unbounded
    """
    # if A*d = 0 and d >= 0 and c'd > 0, then the LP is unbounded
    if np.all(A @ d == 0) and np.all(d >= 0) and c @ d > 0:
        print("A * d = 0: ", A @ d)
        print("d >= 0: ", d)
        print("c'd > 0: ", c @ d)
        print("LP is unbounded")
    else:
        print("LP is not unbounded")

if __name__ == '__main__':
    # Define the matrix A and vector b from the LP
    A = np.array([
        [1, 1, -3, 1, 2],
        [0, 1, -2, 2, -2],
        [-2, -1, 4, 1, 0]
    ])
    b = np.array([7, -2, -3])
    # define c as a numpy vector, objective function c
    c = np.array([-1, 0, 3, 7, 1])

    # define feasible solution x
    x = np.array([2, 0, 0, 1, 2])
    # define feasible direction d (certificate of unboundedness)
    d = np.array([1, 2, 1, 0, 0])

    # check if the LP is unbounded
    check_unbounded(A, b, x, d)