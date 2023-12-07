import os

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def matrix_multiply(mat1, mat2):
    return [
        [sum(a * b for a, b in zip(row, col)) for col in zip(*mat2)] 
        for row in mat1
    ]

def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(len(matrix)):
            submatrix = [row[:i] + row[i+1:] for row in matrix[1:]]
            det += ((-1) ** i) * matrix[0][i] * determinant(submatrix)
        return det

def inverse(matrix):
    det = determinant(matrix)
    if det == 0:
        return None  
    n = len(matrix)
    adjugate = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            minor = [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
            cofactor = ((-1) ** (i + j)) * determinant(minor)
            adjugate[j][i] = cofactor
    scalar = 1 / det
    return [[elem * scalar for elem in row] for row in adjugate]

def process_input(content):
    
    num_matrices, matrix_size = map(int, content[0].split())
    
    matrices_list = []
    for i in range(1, 1 + num_matrices * matrix_size, matrix_size):
        matrix = [list(map(int, line.split())) for line in content[i:i+matrix_size]]
        matrices_list.append(matrix)

    max_det = float('-inf')
    max_det_indices = None
    for i in range(num_matrices):
        for j in range(i + 1, num_matrices):
            det_ij = determinant(matrix_multiply(matrices_list[i], matrices_list[j]))
            if det_ij > max_det:
                max_det = det_ij
                max_det_indices = (i, j)
    if determinant(matrices_list[max_det_indices[0]])==determinant(matrices_list[max_det_indices[1]]):
        result_matrix=matrix_multiply(matrices_list[max_det_indices[0]], matrices_list[max_det_indices[1]])
    elif determinant(matrices_list[max_det_indices[0]])>determinant(matrices_list[max_det_indices[1]]):
        result_matrix = matrix_multiply(matrices_list[max_det_indices[0]], matrices_list[max_det_indices[1]])
    else:
        result_matrix = matrix_multiply(matrices_list[max_det_indices[1]], matrices_list[max_det_indices[0]])
    inverted_matrix = inverse(result_matrix)

    return "\n".join(" ".join(f"{elem:.3f}" for elem in row) for row in inverted_matrix)

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
