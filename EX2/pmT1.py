def generate_pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1]  # The first element in each row is always 1
        for j in range(1, i):
            prev_row = triangle[i - 1]
            new_element = prev_row[j - 1] + prev_row[j]
            row.append(new_element)
        if i > 0:  # Avoid adding an extra 1 at the end of the first row
            row.append(1)
        triangle.append(row)
    return triangle

#def print_pascals_triangle(triangle):
#    for row in triangle:
#        row_str = ' '.join(map(str, row))
#        print(row_str)

#N = int(input())
#triangle = generate_pascals_triangle(N)
#print_pascals_triangle(triangle)

#def generate_pascals_triangle(num_rows):
#    triangle = []

#    for i in range(num_rows):
#        row = [1] * (i + 1)
#        triangle.append(row)

#        if i > 1:
#            for j in range(1, i):
#                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

#    return triangle

#def print_pascals_triangle(triangle):
#    for row in triangle:
#        for num in row:
#            print(num, end=" ")
#        print()

## Set the number of rows you want in Pascal's Triangle
#num_rows = 5

## Generate Pascal's Triangle
#pascals_triangle = generate_pascals_triangle(num_rows)

## Print Pascal's Triangle
#print_pascals_triangle(pascals_triangle)
#