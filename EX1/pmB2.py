# Input two integers
num1 = int(input())
num2 = int(input())

# Add the two integers using logical operators
result = num1
carry = 0

while num2 != 0:
    carry = result & num2
    result = result ^ num2
    num2 = carry << 1

# Input a third integer
third_num = int(input())

# Check if the sum of the first two integers matches the third
if result == third_num:
    print(f"{result}\nYES")
else:
    print(f"{result}\nNO")
