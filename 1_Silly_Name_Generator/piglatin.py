"""Convert words into Pig Latin."""
def main():
    """Get a word from the user, convert it to pig latin and print to screen.
    
    Pig Latin:
    append "way" at the end if the word starts with a vowel, or move the
    first letter to the end and append "ay" if the word starts with a
    consonant.
    """
    while True:
        #Get word from user and store it into a variable
        word = input("\n\nEnter a word to convert it into piglatin: ")
        #Check if input is a valid word
        while len(word) == 0 or word.isdigit():
            word = input("\n\nPlease enter a valid word: ")
        #Check if first character is a vowel
        if word[0] in ("a", "e", "i", "o", "u"):
            #If it IS:
            #append "way" to string
            word = word + "way"
        else:
            #If it's NOT:
            #move first letter to the end and append "ay"
            word = word[1:] + word[0] + "ay"
        print(word)
        #Ask the user to quit or play again
        try_again = input("\n\nTry again? (Press Enter else n to quit) ")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()
