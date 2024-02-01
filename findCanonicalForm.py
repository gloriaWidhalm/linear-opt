from copy import deepcopy

import numpy as np

from data import get_data


def get_canonical_form(A, b, c, z, B):
    # A_B is the basis part of A (sub-matrix of A with columns in B)
    A_B = A[:, B]
    # c_B is the part of c corresponding to the basis
    c_B = c[B]
    # Calculate y (the inverse of A_B times c_B, need it to calculate z)
    y = np.linalg.inv(A_B.T) @ c_B
    # get new z (objective value)
    z = y @ b + z
    # get new c (objective function)
    c = c - A.T @ y
    # modify b and A (update to get the canonical form)
    b = np.linalg.inv(A_B) @ b
    A = np.linalg.inv(A_B) @ A
    return A, b, c, z


def get_canonical_form_with_x(A, b, c, z, B):
    # A_B is the basis part of A (sub-matrix of A with columns in B)
    A_B = A[:, B]
    # c_B is the part of c corresponding to the basis
    c_B = c[B]
    # Calculate y (the inverse of A_B times c_B, need it to calculate z)
    y = np.linalg.inv(A_B.T) @ c_B
    # get new z (objective value)
    z = y @ b + z
    # get new c (objective function)
    c = c - A.T @ y
    # modify b and A (update to get the canonical form)
    b = np.linalg.inv(A_B) @ b
    A = np.linalg.inv(A_B) @ A

    # get x
    # x = x_B + x_N
    x_B = b
    x_N = np.zeros(len(c) - len(B))
    # insert according to basis
    for i in range(len(B)):
        x_N = np.insert(x_N, B[i], x_B[i])
    x = x_N
    return A, b, c, z, x


def print_problem_information(A, b, c, z, x=None, B=None):
    if B is not None:
        print("Canonical form for the basis B: ", B)
        print("caution: 0-based indexing, so the first column is column 0, the actual basis is B+1 (if we did it by hand)")
    print("A: ", A)
    print("b: ", b)
    print("c: ", c)
    print("z: ", z)
    if x is not None:
        print("x: ", x)


if __name__ == '__main__':
    # initialize z (objective value)
    z = 0

    # get A, b, c
    A, b, c = get_data()

    print_problem_information(A, b, c, z)

    # basis
    B = np.array([2, 4])
    # B3_1 = np.array([2, 4])

    # get canonical form
    A, b, c, z, x = get_canonical_form_with_x(A, b, c, z, B)
    print("----- Solution -----")
    print_problem_information(A, b, c, z, x, B)
