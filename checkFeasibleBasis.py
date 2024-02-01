import numpy as np


# This function is based on the slides from the course
def check_feasible_basis(A, x, b, B=None):
    """
    Check if the basis B is feasible for the LP defined by A and b
    """
    # A vector x is a basic solution, if Ax = b and x_N = 0
    # where x_N is the vector of non-basic variables

    print("Checking for x: ", x)

    # if B is not given, use the non-zero entries of x as the basis
    if B is None:
        # use nonnegative entries of x as the basis
        B = np.where(x > 0)[0]
        # check if the number of non-zero entries in x is equal to the number of rows in A
        if len(B) != A.shape[0]:
            print('The number of non-zero entries in x is not equal to the number of rows in A, check by hand')
            return
        print("B: ", B)

    # get the non-basic variables
    N = np.setdiff1d(np.arange(A.shape[1]), B)
    print("N: ", N)
    x_N = x[N]
    print("x_N: ", x_N)

    # check if B is a basis for A
    if check_basis(A, B):
        print('B is a basis for A')
    else:
        print('B is not a basis for A, not a feasible solution')
        return

    if np.all(A @ x == b) and np.all(x_N == 0):
        print('Ax = b')
        print('x_N = 0')
        print('Basic solution')
    else:
        print('x is not a basic solution')
        print('Ax != b or x_N != 0: ', A @ x, b, "x_N: ", x_N)
        return

    # if x >= 0, then x is a basic feasible solution
    if np.all(x >= 0):
        print('x >= 0')
        print('Basic feasible solution')
    else:
        print('x is not non-negative, not a basic feasible solution')


# This function checks if the basis is feasible by calculating the inverse of the basis sub-matrix, if not possible, then the basis is not feasible
def check_feasible_basis1(A, b, B):
    """
    Check if the basis B is feasible for the LP defined by A and b
    """

    # Calculate the inverse of the basis sub-matrix and then the basic feasible solution x_B
    A_B = A[:, B]
    try:
        A_B_inv = np.linalg.inv(A_B)
        x_B = A_B_inv @ b
    except np.linalg.LinAlgError:
        print("Basis is not feasible")
        x_B = None  # If A_B is singular, inverse does not exist

    return x_B


def check_basis(A, B):
    """
    Check if the given basis forms a basis for the matrix A
    """

    print("Basis: ", B)

    # if the determinant of the basis sub-matrix is non-zero, then the basis is valid
    A_B = A[:, B]
    if np.linalg.det(A_B) != 0:
        print("det(A_B) != 0 ", np.linalg.det(A_B))
        print('The basis is valid')
    else:
        print("det(A_B) = 0 ", np.linalg.det(A_B))
        print('The basis is invalid')


if __name__ == '__main__':
    print('Check if a basis is valid for a given matrix A')
    # check whether a given basis forms a basis for the matrix A
    A = np.array([
        [2, 1, 2, -1, 0, 0],
        [1, 0, -1, 2, 1, 0],
        [3, 0, 3, 1, 0, 1]
    ])

    B1 = [0, 1, 2]
    B2 = [0, 4, 5]
    B4 = [0, 2, 4]

    check_basis(A, B1)
    check_basis(A, B2)
    check_basis(A, B4)

    print("---------------------------")


    print('Check if a basis is feasible for a given LP')
    # Define the matrix A and vector b from the LP
    A = np.array([
        [1, 1, 0, 2, 1, 1, 1],
        [0, 2, 2, 0, 0, -2, 1],
        [1, 2, 1, 5, 4, 3, 3]
    ])

    b = np.array([2, 2, 6])

    # feasible solution x
    x = np.array([1, 1, 0, 0, 0, 0, 0])


    print("Check with first version of check_feasible_basis")
    check_feasible_basis(A, x, b)


    # Basis B
    B = [2, 3, 4]  # Using zero-based indexing for Python

    # Check if the basis B is feasible
    print("Check with second version of check_feasible_basis")
    x_B = check_feasible_basis1(A, b, B)
