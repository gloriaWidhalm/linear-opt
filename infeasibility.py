# write a function that checks if a given solution is infeasible (Farkas' Lemma)

import numpy as np


def check_infeasibility(A, b, y):
    """
    Check if the problem is infeasible for the LP defined by A and b
    """
    # if y' * A >= 0 and y'b < 0, then the LP is infeasible
    if np.all(y @ A >= 0) and y @ b < 0:
        print("y' * A: >= 0:", y @ A)
        print("y' * b < 0: ", y @ b)
        print("LP is infeasible")
    else:
        print("LP is not infeasible")

if __name__ == '__main__':
    # Define the matrix A and vector b from the LP
    A = np.array([
        [4, 10, -6, -2],
        [-2, 2, -4, 1],
        [-7, -2, 0, 4]
    ])
    b = np.array([6, 5, 3])
    # Define y (certificate of infeasibility)
    y = np.array([1, -2, 1])

    # Check if x is infeasible
    check_infeasibility(A, b, y)