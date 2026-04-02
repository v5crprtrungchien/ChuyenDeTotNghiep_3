import numpy as np

A = np.array([
    [2, 1],
    [1, 3]
])
B = np.array([
    [4, 2],
    [1, 5]
])

print("A + B =\n", A + B)
print("A - B =\n", A - B)
print("A @ B =\n", A @ B)

det_A = np.linalg.det(A)
inv_A = np.linalg.inv(A)
print("det(A) =", det_A)
print("A^-1 =\n", inv_A)

b = np.array([5, 7])
solution = np.linalg.solve(A, b)
print("Nghiệm hệ phương trình:", solution)