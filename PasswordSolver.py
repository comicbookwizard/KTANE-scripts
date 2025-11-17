import copy

PASSWORD_WORDS = [
    "about","after","again","below","could","every","first","found","great","house",
    "large","learn","never","other","place","plant","point","right","small","sound",
    "spell","still","study","their","there","these","thing","think","three","water",
    "where","which","world","would","write"
]

def solve_password():
    """
    Determines which password to input in the 'Password' module of Keep Talking and Nobody Explodes.
    All the logic is taken from the Manual at https://www.bombmanual.com/web/.
    
    Prints out possible words after each input of possible letters for each position.s
    """

    print("=== PASSWORD MODULE SOLVER ===")
    print("Enter possible letters for each position (e.g. abc for first column).")
    print("After each input, you'll see which words are still possible.\n")

    possible_words = copy.deepcopy(PASSWORD_WORDS)
    for i in range(5):
        letters = input(f"Position {i+1} possible letters: ").strip().lower()

        possible_words = [w for w in possible_words if w[i] in letters]
        print("\nPossible words:")
        if possible_words:
            for w in possible_words:
                print(" -", w)
        else:
            print("No words fit those letters. Check your input.")
            break

        if len(possible_words) == 1:
            print(f"\nThe password is: {possible_words[0].upper()}")
            return

        print("\n----------------------------")

    if len(possible_words) > 1:
        print(f"\nMultiple possibilities remain: {', '.join(possible_words)}. Check your inputs and try again.")
    elif len(possible_words) == 1:
        print(f"\nThe password is: {possible_words[0].upper()}")
    else:
        print("\nNo matching words found. Double-check your inputs.")


if __name__ == "__main__":
    solve_password()
