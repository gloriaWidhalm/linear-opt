import numpy as np
# function that computes the eigenvalues of a matrix and checks if it is positive definite
def is_pos_def(x):
    print("eigenvalues of the matrix are: ", np.linalg.eigvals(x))
    return np.all(np.linalg.eigvals(x) > 0)


if __name__ == "__main__":
    # create a matrix
    B = np.array([[1, 0], [0, 1]])
    print("matrix: ", B)
    # call the function
    print("is convex: ", is_pos_def(B))

    # create a matrix
    B = np.array([[2, 5], [5, 2]])
    print("matrix: ", B)
    # call the function
    print("is convex: ", is_pos_def(B))
    # get determinant of matrix
    print("determinant of matrix is: ", np.linalg.det(B))

    A = np.array(
        [[-84, 126, -66], [126, -414, -156], [-66, -156, -414]]
    )
    print("matrix: ", A)
    # call the function
    print("is convex: ", is_pos_def(A))