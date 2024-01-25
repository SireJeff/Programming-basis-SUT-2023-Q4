import re

def remove_persian_special_characters(text):
    # Define a regular expression pattern for Persian special characters
    persian_special_chars_pattern = re.compile(r'[،:؛.؟!٬٫]+')

    # Replace Persian special characters with an empty string
    cleaned_text = persian_special_chars_pattern.sub('', text)

    return cleaned_text
def find_similar_words(n, sentence, target_word):
    #sentence=sentence.strip(",./';:!?")
    sentence=remove_persian_special_characters(sentence)
    words = sentence.split(" ")
    #print(f"{sentence}\n{words}")
    result = []

    for word in words:
        distance = calculate_distance(word, target_word)
        if distance <= n:
            result.append(word)

    return result

def calculate_distance(word1, word2):
    len1, len2 = len(word1), len(word2)
    if len1 < len2:
        word1 += '_' * (len2 - len1)
    elif len1 > len2:
        word2 += '_' * (len1 - len2)


    distance = sum(c1 != c2 for c1, c2 in zip(word1, word2))

    return distance

# Example usage
n = int(input())
sentence = input()
target_word = input()

result = find_similar_words(n, sentence, target_word)
for word in result:
    print(word)
