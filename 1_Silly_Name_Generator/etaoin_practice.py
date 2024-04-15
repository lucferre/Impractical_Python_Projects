"""Count the numbers of letters in a phrase and return a barchart."""

def main():
    """Get a phrase and print to screen a barchar with each letter's count.
    
    The purpose is to demonstrate that ETAOIN are the most commonly used
    letters in the English language.
    If no phrase is provided by the user, a default phrase will be used.
    """
    barchart = {}
    text = input("\n\nEnter a phrase: ")
    if text == "":
        text = "Like the castle in its corner in a medieval game, I foresee \
terrible trouble and I stay here just the same."

    print(f"\n\n{text}\n\n")
    for letter in text:
        letter = letter.lower()
        #print(letter, end=" ")
        if letter in barchart:
            barchart[letter].append(letter)
        elif letter.isalpha():
            barchart[letter] = [letter]

    sorted_barchart = dict(sorted(barchart.items()))

    for key in sorted_barchart:
        print(f"{key}: {sorted_barchart[key]} {len(sorted_barchart[key])}")

if __name__ == "__main__":
    main()
