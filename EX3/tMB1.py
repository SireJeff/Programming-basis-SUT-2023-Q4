def decode_letter(encoded_str):
    parts = encoded_str.split()
    parts.sort(key=lambda x: int(x[1:]))
    decoded_str = ''.join([part[0] for part in parts])
    return decoded_str

# Get user input for the encoded string
encoded_input = input()

# Decode the string and print the result
decoded_output = decode_letter(encoded_input)
print(decoded_output)
