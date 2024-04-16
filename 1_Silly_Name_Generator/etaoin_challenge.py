"""Count the numbers of letters in a phrase and print a barchart."""

def main():
    """Get a phrase and print to screen a barchar with each letter's count.
    
    The purpose is to demonstrate that ETAOIN are the most commonly used
    letters in the English language.
    If no phrase is provided by the user, a default phrase will be used.
    This version has been adapted to display all the letters of the alphabet,
    even when they are not present in the phrase.
    """
    barchart = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g':[],
'h': [], 'i': [], 'j': [], 'k': [], 'l': [], 'm': [], 'n': [], 'o': [],
'p': [], 'q': [], 'r': [], 's':[], 't': [], 'u': [], 'v': [], 'w': [], 'x': [],
'y': [], 'z': []}

    text = input("\n\nEnter a phrase: ")
    if text == "":
        text = "Like the castle in its corner in a medieval game, I foresee \
terrible trouble and I stay here just the same."

    print(f"\n\n{text}\n\n")
    for letter in text:
        if letter.isalpha():
            letter_lower = letter.lower()
            barchart[letter_lower].append(letter_lower)

    for key, item in barchart.items():
        print(f"{key}: {item} {len(item)}")

if __name__ == "__main__":
    main()
