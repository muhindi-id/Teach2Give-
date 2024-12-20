def capitalize_words(input_string):

    result = input_string.title()
    return result

input_string = input("Enter a string: ")
output = capitalize_words(input_string)
print("Capitalized String:", output)
