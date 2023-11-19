def format_text(input_text):
    # Split the text into a list of characters
    char_list = list(input_text)

    # Iterate through the characters and remove extra '#' after '@'
    i = 0
    while i < len(char_list):
        if char_list[i] == '@':
            j = i + 1
            while j < len(char_list):
                if char_list[j] == '#':
                    char_list.pop(j)
                    break
                else:
                    j += 1
            i += 1
        else:
            i += 1

    # Join the characters back into a string
    formatted_text = ''.join(char_list)

    # Remove extra spaces
    formatted_text = ' '.join(formatted_text.split())

    # Handle new lines after "n\"
    #formatted_text = formatted_text.replace('n\\', '\n')

    # Replace escape sequences
    formatted_text = formatted_text.replace("\\n", "\n")
    formatted_text = formatted_text.replace("\\t", "\t")

    return formatted_text

# Get input from the user
user_input = input()

# Call the function and print the result
formatted_text = format_text(user_input)
print(f"Formatted Text: {formatted_text}")
