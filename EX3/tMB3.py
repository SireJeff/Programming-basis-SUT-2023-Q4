import codecs
def format_text(input_text):
    # Remove # after @
    formatted_text = input_text.replace('@#', '@')

    # Remove specified # characters
    formatted_text = formatted_text.replace('#', '')

    # Remove extra spaces
    formatted_text = ' '.join(formatted_text.split())

    # Handle new lines after "n\"
    formatted_text = formatted_text.replace('n\\', '\n')

    return formatted_text

# Get input from the user
user_input = input()
# Call the function and print the result
formatted_text = format_text(user_input)
user_inputt = codecs.decode(formatted_text, 'unicode_escape')
print(f"Formatted Text: {user_inputt}")
