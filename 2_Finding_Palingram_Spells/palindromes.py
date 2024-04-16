"""Find palindromes (letter palingrams) in a dictionary file."""
import load_dictionary
# Assign empty list to a variable to store palindromes
pali_list = []
# Load dictionary file
word_list = load_dictionary.load('words.txt')

# Loop through each word in the file
for word in word_list:
# Assign the reversed word to a varible
    reversed_word = word[::-1]
# If word and reversed word are equal:
    if word == reversed_word:
    # append the word to a list of palindromes
        pali_list.append(word)
        
# Print to screen the array of palindromes
print(f"Number of palindromes found = {len(pali_list)}\n")
print(*pali_list, sep='\n')