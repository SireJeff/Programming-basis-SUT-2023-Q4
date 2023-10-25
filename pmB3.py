def int_to_binary_32bit(num):
    # Convert the integer to a 32-bit binary string
    binary_string = bin(num)[2:].zfill(32)
    return binary_string

# Input two integers
num1 = int(input())
num2 = int(input())

# Convert integers to 32-bit binary strings
binary_string1 = int_to_binary_32bit(num1)
binary_string2 = int_to_binary_32bit(num2)

# Concatenate the two binary strings to form a 64-bit binary string
concatenated_binary = binary_string2 + binary_string1

# Print the concatenated binary string
#print(concatenated_binary)
binary_array = [int(bit) for bit in concatenated_binary.zfill(64)]
F=int(input())
checks=[]
for i in range(F):
    checks.append(int(input()))
for j,i in enumerate (checks):
    for idx, nu in enumerate(binary_array): # the pythonic way to get the indices
        if 63-idx==i and nu==1:
            print("yes")
        elif 63-idx==i and nu==0:
            print("no")
     