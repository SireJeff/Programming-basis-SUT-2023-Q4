# Matrix Inversion

This Python script calculates and prints the inverted matrix based on a set of matrices provided in an input file. The inversion process is performed by finding the pair of matrices that yields the maximum determinant when multiplied, and then computing the inverted matrix from their dot product.

## Usage

1. **Input Files**: Place input files in the `./in/` directory. Each input file should contain the number of matrices, the size of each matrix, and the matrix values.

   Example input file (`input_example.txt`):
   ```
   2 2
   1 2
   3 4
   5 6
   7 8
   ```

2. **Running the Script**: Execute the script by running `python script_name.py`. The script will process all input files in the `./in/` directory and generate corresponding output files in the `./outputs/` directory.

   ```bash
   python script_name.py
   ```

3. **Output Files**: Output files will be created in the `./outputs/` directory, named as `output_input_file_name`. Each output file contains the inverted matrix for the corresponding input.

   Example output file (`output_input_example.txt`):
   ```
   -2.000 1.000
   1.500 -0.500
   ```

## Code Explanation

### `calculate_and_print_inverted_matrix`

This function takes the number of matrices, the size of each matrix, and a list of matrices as input. It calculates the pair of matrices that yield the maximum determinant when multiplied, computes the result matrix, and then calculates and prints the inverted matrix.

### `arrangeinput`

This function processes the content of an input file, extracting the number of matrices, the size of each matrix, and the matrix values. It then calls `calculate_and_print_inverted_matrix` with the extracted information.

### `main`

The main function orchestrates the entire process. It reads input files from the `./in/` directory, processes each file, and writes the corresponding output files to the `./outputs/` directory.

## Input File Format

- The first line contains two space-separated integers: the number of matrices (`num_matrices`) and the size of each matrix (`matrix_size`).
- The following lines contain the matrix values, where each line represents a row in the matrix.

   Example:
   ```
   2 2
   1 2
   3 4
   5 6
   7 8
   ```

## Output File Format

- The output file contains the inverted matrix with each element formatted to three decimal places.

   Example:
   ```
   -2.000 1.000
   1.500 -0.500
   ```

## Dependencies

- The script relies on the following Python libraries: `os`, `pandas`, and `numpy`. Ensure they are installed before running the script.

   ```bash
   pip install pandas numpy
   ```

## Notes

- Make sure to provide valid input files in the `./in/` directory before running the script.
- The script automatically creates the `./outputs/` directory if it does not exist.
- Output files are named by prefixing "output_" to the input file name.