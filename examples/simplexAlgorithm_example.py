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
    num_variables = A.shape[1]
    num_slack_variables = A.shape[0]
    basis = initial_basis

    # Step 1: Convert to canonical form (assume a basic feasible solution)
    A, b, c, z = get_canonical_form(A, b, c, z, basis)

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
        return A, b, c, z, basis

    # Step 3: Select an entering variable (index k from non-basic variables)
    # Bland's rule: Select the first index k such that c_k > 0
    k_index = np.where(c[non_basic_indices] > 0)[0][0]
    k = non_basic_indices[k_index]  # This is the actual index in 'A'

    # Step 4: Check if A_k <= 0, which means the LP is unbounded
    A_k = A[:, k]
    if np.all(A_k <= 0):
        print("LP is unbounded: ", A_k, k)
        return A, b, c, z, basis

    # Step 5: Determine the leaving variable (index r)
    ratios = np.divide(b, A_k, out=np.full_like(b, np.inf, dtype=float), where=A_k > 0)
    r = np.argmin(ratios)
    print("ratios: ", ratios)
    print("t (=smallest ratio): ", ratios[r])

    # Step 6 and 7: Perform the pivot
    # Replace the r-th basis element with the entering variable k
    basis[r] = k

    # Step 8 -> if there is an improvement, run the algorithm again

    # after iteration of simplex algorithm
    print("AFTER iteration of simplex algorithm: ")
    print("A: ", A)
    print("b: ", b)
    print("c: ", c)
    print("z: ", z)
    print("basis: ", basis)
    return A, b, c, z, basis


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

    # example 2
    A = np.array([
        [2, 5, 1, 0, 3, 1],
        [0, 2, 2, -4, 2, -4],
        [3, 5, 1, 2, 6, 3]
    ])
    b = np.array([9 / 4, 0, 4])
    c = np.array([2, -4, 1, 4, 8, 4])

    # objective value
    z = 0
    # define the initial basis
    initial_basis = np.array([0, 2, 3])
    print("BEFORE SIMPLEX ALGORITHM: ")
    print_problem_information(A, b, c, z)

    # Perform the Simplex algorithm
    A, b, c, z, basis = simplex_algorithm(A, b, c, z, initial_basis)
    print("**NEXT ITERATION**")
    # Perform the Simplex algorithm
    A, b, c, z, basis = simplex_algorithm(A, b, c, z, basis)
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
