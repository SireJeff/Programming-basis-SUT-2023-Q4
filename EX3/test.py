
input_string = input("Enter a string: ")
result = ""
for char in input_string:

        ascii_value = ord(char)

       
        processed_char = char.upper() if ascii_value > 80 else char

       
        result += processed_char

print("Processed String:", result)
