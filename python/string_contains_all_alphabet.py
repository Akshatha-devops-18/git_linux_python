# Import the 'string' module to access the lowercase alphabet.
import string
#check whether a string contains all letters of alphabet
# Create a set 'alphabet' containing all lowercase letters using 'string.ascii_lowercase'.
alphabet = set(string.ascii_lowercase)

# Define an input string.
input_string = 'The quick brown fox jumps over the lazy dog'

# Check if the set of lowercase characters in the input string contains all the letters of the alphabet.
# Print the result (True or False).
print(set(input_string.lower()) >= alphabet)

# Update the input string.
input_string = 'The quick brown fox jumps over the lazy cat'

# Check if the set of lowercase characters in the updated input string contains all the letters of the alphabet.
# Print the result (True or False).
print(set(input_string.lower()) >= alphabet)


#output:
True
False