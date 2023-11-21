import re
decimal_number_str = input("Enter a decimal number: ")
filtered_string = re.sub(r'[^0-9a-fA-F]', '', decimal_number_str)

print("Hexadecimal Representation:", filtered_string)
