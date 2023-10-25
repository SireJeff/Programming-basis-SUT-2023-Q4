def count_bits_to_change(num1, num2):
    # Calculate the XOR of the two numbers
    xor_result = num1 ^ num2

    # Initialize a count to keep track of the set bits
    count = 0

    # Count the set bits in the XOR result
    while xor_result:
        count += xor_result & 1
        xor_result >>= 1

    return count

# Input two numbers
num1 =int(input())
num2 = int(input())

# Calculate and print the number of bits to change
bits_to_change = count_bits_to_change(num1, num2)
print(bits_to_change)
