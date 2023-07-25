# You are to write a Python function named nickname_generator. This function should take a single argument, name, 
# which is a string, and return a nickname based on the following rules:

# If the third letter of name is a consonant, the function should return the first three letters as the nickname.
# For example, 
# nickname_generator("Robert") should return "Rob".

# If the third letter of name is a vowel, the function should return the first four letters as the nickname. 
# For example, 
# nickname_generator("Jeannie") should return "Jean".

# If the string name has fewer than four characters, the function should return the string "Error: Name too short".
# Notes:

# For the purposes of this exercise, consider the vowels to be "aeiou". The letter "y" should be treated as a consonant.

# The input will always be a string, with the first letter capitalized and the rest in lowercase (e.g., "Sam"). 

#Pseudo

# index into third letter (third letter consonant = return first 3 letters)

# length of name (third letter vowel = return first four letters)

# length of name < 4 characters = return "Error: Name too short"


def nickname_generator(name):
    vowels = 'aeiou'
    if len(name) < 4:
        return 'Error: Name too short'
    if name[2] in vowels:
        return name[:4]
    else:
        return name[:3]

print(nickname_generator('Jeannie'))
print(nickname_generator('Robert'))
print(nickname_generator('Bo'))
