import numpy as np

num_matrices, matrix_size = map(int, input().split())

matrices_list = []
for _ in range(num_matrices):
    matrix = [list(map(int, input().split())) for _ in range(matrix_size)]
    matrices_list.append(np.array(matrix))

max_det = float('-inf')
max_det_indices = None
for i in range(num_matrices):
    for j in range(i + 1, num_matrices):
        det_ij = np.linalg.det(np.dot(matrices_list[i], matrices_list[j]))
        if det_ij > max_det:
            max_det = det_ij
            max_det_indices = (i, j)

result_matrix = np.dot(matrices_list[max_det_indices[0]], matrices_list[max_det_indices[1]])

inverted_matrix = np.linalg.inv(result_matrix)

for row in inverted_matrix:
    print(" ".join(f"{elem:.3f}" for elem in row))
