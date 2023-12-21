import os
import pandas as pd
import numpy as np

def calculate_and_print_inverted_matrix(num_matrices, matrix_size, matrices_list):
    def calculate_det_and_dot_product(matrix1, matrix2):
        return np.linalg.det(np.dot(matrix1, matrix2))

    def find_max_det_indices():
        max_det = float('-inf')
        indices = None

        for i in range(num_matrices):
            for j in range(i + 1, num_matrices):
                det_ij = calculate_det_and_dot_product(matrices_list[i], matrices_list[j])
                if det_ij > max_det:
                    max_det = det_ij
                    indices = (i, j)

        return indices

    def calculate_result_matrix(index_a, index_b):
        det_a = np.linalg.det(matrices_list[index_a])
        det_b = np.linalg.det(matrices_list[index_b])

        if det_a == det_b:
            return np.dot(matrices_list[index_a], matrices_list[index_b])
        elif det_a > det_b:
            return np.dot(matrices_list[index_a], matrices_list[index_b])
        else:
            return np.dot(matrices_list[index_b], matrices_list[index_a])

    def calculate_inverted_matrix(result_matrix):
        return np.linalg.inv(result_matrix)

    max_det_indices = find_max_det_indices()
    result_matrix = calculate_result_matrix(*max_det_indices)
    inverted_matrix = calculate_inverted_matrix(result_matrix)

    return "\n".join(" ".join(f"{elem:.3f}" for elem in row) for row in inverted_matrix)


def arrangeinput(content):
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

        result = arrangeinput(content)

        with open(output_path, 'w') as file:
            file.write(result)
# def main():
#     input_file_path = "ifile.txt"  
#     output_file_path = "ofile.txt" 

#     with open(input_file_path, 'r') as file:
#         content = file.read().splitlines()

#     num_mats, mat_size = map(int, content[0].split())

#     mats_list = []
#     for i in range(1, 1 + num_mats * mat_size, mat_size):
#         matrix = [list(map(int, line.split())) for line in content[i:i + mat_size]]
#         mats_list.append(np.array(matrix))

#     result = varmatrix(num_mats, mat_size, mats_list)

#     with open(output_file_path, 'w') as file:
#         file.write(result)
if __name__ == "__main__":
    main()
