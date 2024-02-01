import numpy as np
import scipy

from data import get_data
from findCanonicalForm import get_canonical_form, print_problem_information


def simplex_algorithm(A, b, c, z, initial_basis):
    """
    Perform the Simplex algorithm to solve the given linear program
    These steps are the same as in the lecture slides (not tableau form)
    """

    # Initialize basis with the indices of the slack variables

    # make sure that the basis is always the last columns of A
    rearrange_basis(A, c, initial_basis)
    print("A: ", A)
    print("c: ", c)
    print("initial basis: ", initial_basis)

    num_variables = A.shape[1]
    num_slack_variables = A.shape[0]
    print("num variables: ", num_variables)
    print("num slack variables: ", num_slack_variables)
    basis = list(range(num_variables - num_slack_variables, num_variables))
    print("basis: ", basis)
    print(list(range(num_variables - num_slack_variables, num_variables)))

    # Step 1: Convert to canonical form (assume a basic feasible solution)
    A, b, c, z, x = get_canonical_form(A, b, c, z, basis)
    print("after get_canonical_form: ")
    print("A: ", A)
    print("b: ", b)
    print("c: ", c)
    print("z: ", z)

    # Step 2: Check if current solution is optimal (if all c_N <= 0)
    non_basic_indices = [i for i in range(num_variables) if i not in basis]
    c_N = c[non_basic_indices]
    if np.all(c_N <= 0):
        # If all c_N are non-positive, the current solution is optimal
        x = np.zeros(num_variables)
        x[basis] = np.linalg.inv(A[:, basis]) @ b
        print("Optimal solution found")
        print("x: ", x, "basis: ", basis)
        print("z: ", z)
        return
        #return x, z, "Optimal solution found"

    # Step 3: Select an entering variable (index k from non-basic variables)
    # Bland's rule: Select the first index k such that c_k > 0
    k_index = np.where(c[non_basic_indices] > 0)[0][0]
    k = non_basic_indices[k_index]  # This is the actual index in 'A'

    # Step 4: Check if A_k <= 0, which means the LP is unbounded
    A_k = A[:, k]
    if np.all(A_k <= 0):
        print("LP is unbounded: ", A_k, k)
        # return None, None, "LP is unbounded"

    # Step 5: Determine the leaving variable (index r)
    ratios = np.divide(b, A_k, out=np.full_like(b, np.inf, dtype=float), where=A_k > 0)
    r = np.argmin(ratios)

    # Step 6 and 7: Perform the pivot
    # Replace the r-th basis element with the entering variable k
    basis[r] = k

    # Step 8 -> if there is an improvement, run the algorithm again


def rearrange_basis(A, c, basis):
    """
    Rearrange the matrix A, and cost vector c, such that the columns corresponding to the basis are always the last
    """
    # Get the indices of the non-basic variables
    non_basic_indices = [i for i in range(A.shape[1]) if i not in basis]

    # Rearrange the columns of A and c such that the columns corresponding to the basis are always the last
    # This is done by concatenating the columns of A and c corresponding to the non-basic variables with the columns
    # corresponding to the basic variables
    A = np.concatenate((A[:, non_basic_indices], A[:, basis]), axis=1)
    c = np.concatenate((c[non_basic_indices], c[basis]))

    return A, c


if __name__ == "__main__":
    print("Simplex Algorithm")
    print("Caution: This implementation is only step-by-step, there is no loop, so if there is an improvement, you have to run the algorithm again")

    # Define the matrix A, vector b, and cost vector c
    A = np.array([
        [-1, 1, 0, 2],
        [1, 0, 1, -3]
    ])
    b = np.array([2, 1])
    c = np.array([-1, 0, 0, 2])

    # objective value
    z = 0
    # define the initial basis
    initial_basis = np.array([1, 2])

    # get canonical form
    A, b, c, z, x = get_canonical_form(A, b, c, z, initial_basis)
    print("BEFORE SIMPLEX ALGORITHM: ")
    print_problem_information(A, b, c, z, x)

    # Perform the Simplex algorithm
    simplex_algorithm(A, b, c, z, initial_basis)
    # solution, objective_value, status = simplex_algorithm(A, b, c, z, initial_basis)
    #
    # print(f"Status: {status}")
    # if solution is not None:
    #     print(f"Solution: {solution}")
    #     print(f"Objective Value: {objective_value}")

    print("--------------------------")
    #
    # # check if the simplex algorithm is correct and compare to the solution from scipy (highs, because simplex is deprecated)
    # # assume we have a canonical form
    # solution_scipy = scipy.optimize.linprog(c, A_eq=A, b_eq=b, method="highs")
    #
    # print("solution scipy: ", solution_scipy.x)
    # # print objective value
    # print("objective value scipy: ", solution_scipy.fun)
