import numpy as np


# function that checks if the solution x is feasible for the LP defined by A and b
def check_feasible_solution(A, b, x, constraint_type='<='):
    print("constraint type: ", constraint_type)
    """
    Check if the solution x is feasible for the LP defined by A and b
    """
    # x is a feasible solution, if it satisfies all constraints

    # check if all entries of x are non-negative
    if np.all(x >= 0):
        print('All entries of x are non-negative')
    else:
        print('x is not non-negative, not a feasible solution')
        return

    # Check if Ax <= b
    if constraint_type == '<=':
        if np.all(A @ x <= b):
            print('A @ x <= b ', A @ x, b)
            print('The solution x is feasible')
            return
    if constraint_type == '>=':
        if np.all(A @ x >= b):
            print('A @ x >= b ', A @ x, b)
            print('The solution x is feasible')
            return
    if constraint_type == '=':
        print('A @ x == b ', A @ x, b)
        if np.all(A @ x == b):
            print('The solution x is feasible')
            return
    print('The solution x is not feasible')


if __name__ == '__main__':
    print('Check if a solution is feasible for a given LP')
    # Define the matrix A and vector b from the LP
    A = np.array([
        [-1, 1, 0, 2],
        [1, 0, 1, -3]
    ])

    b = np.array([2, 1])

    # Define a solution x
    x = np.array([0, 2, 1, 0])
    print("caution: check if the constraints align with your problem (e.g. <= or >=)")

    # Check if the solution x is feasible
    check_feasible_solution(A, b, x, constraint_type='=')
