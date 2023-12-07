import numpy as np

num_matrices, matrix_size = map(int, input().split())

all_matrices = []
for _ in range(num_matrices):
    matrix = [list(map(int, input().split())) for _ in range(matrix_size)]
    all_matrices.append(np.array(matrix))

max_determinant = float('-inf')
max_determinant_pair = None
for i in range(num_matrices):
    for j in range(i + 1, num_matrices):
        determinant_ij = np.linalg.det(np.dot(all_matrices[i], all_matrices[j]))
        if determinant_ij > max_determinant:
            max_determinant = determinant_ij
            max_determinant_pair = (i, j)

resultant_matrix = np.dot(all_matrices[max_determinant_pair[0]], all_matrices[max_determinant_pair[1]])

inverted_resultant_matrix = np.linalg.inv(resultant_matrix)

for row in inverted_resultant_matrix:
    print(" ".join(f"{elem:.3f}" for elem in row))
