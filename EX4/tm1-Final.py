import os
import pandas as pd
import numpy as np

def calculate_and_print_inverted_matrix(num_matrices, matrix_size, matrices_list):
    max_det = float('-inf')
    max_det_indices = None

    for i in range(num_matrices):
        for j in range(i + 1, num_matrices):
            det_ij = np.linalg.det(np.dot(matrices_list[i], matrices_list[j]))
            if det_ij > max_det:
                max_det = det_ij
                max_det_indices = (i, j)

    matrix_a_det = np.linalg.det(matrices_list[max_det_indices[0]])
    matrix_b_det = np.linalg.det(matrices_list[max_det_indices[1]])

    if matrix_a_det == matrix_b_det:
        result_matrix = np.dot(matrices_list[max_det_indices[0]], matrices_list[max_det_indices[1]])
    elif matrix_a_det > matrix_b_det:
        result_matrix = np.dot(matrices_list[max_det_indices[0]], matrices_list[max_det_indices[1]])
    else:
        result_matrix = np.dot(matrices_list[max_det_indices[1]], matrices_list[max_det_indices[0]])

    inverted_matrix = np.linalg.inv(result_matrix)
    return "\n".join(" ".join(f"{elem:.3f}" for elem in row) for row in inverted_matrix)

def process_input(content):
    num_matrices, matrix_size = map(int, content[0].split())

    matrices_list = []
    for i in range(1, 1 + num_matrices * matrix_size, matrix_size):
        matrix = [list(map(int, line.split())) for line in content[i:i + matrix_size]]
        matrices_list.append(np.array(matrix))

    return calculate_and_print_inverted_matrix(num_matrices, matrix_size, matrices_list)

def main():
    input_directory = "./in/"
    output_directory = "./outputs/"
    os.makedirs(output_directory, exist_ok=True)

    input_files = [f for f in os.listdir(input_directory) if os.path.isfile(os.path.join(input_directory, f))]

    for input_file in input_files:
        input_path = os.path.join(input_directory, input_file)
        output_path = os.path.join(output_directory, f"output_{input_file}")

        with open(input_path, 'r') as file:
            content = file.read().splitlines()

        result = process_input(content)

        with open(output_path, 'w') as file:
            file.write(result)

if __name__ == "__main__":
    main()
