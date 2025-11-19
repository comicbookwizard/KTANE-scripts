TABLE = {
    True: {  # Logic for if serial has vowel
        0: {"red":"blue","blue":"red","green":"yellow","yellow":"green"}, # 0 strikes
        1: {"red":"yellow","blue":"green","green":"blue","yellow":"red"}, # 1 strike
        2: {"red":"green","blue":"red","green":"yellow","yellow":"blue"}, # 2 strikes
    },
    False: { # Logic for if serial has no vowel
        0: {"red":"blue","blue":"yellow","green":"green","yellow":"red"}, # 0 strikes
        1: {"red":"red","blue":"blue","green":"yellow","yellow":"green"}, # 1 strike
        2: {"red":"yellow","blue":"green","green":"blue","yellow":"red"}, # 2 strikes
    }
}

def translate_sequence(sequence, vowel, strikes):
    """
    Determines which buttons to press in the 'Simon Says' module of Keep Talking and Nobody Explodes.
    All the logic is taken from the Manual at https://www.bombmanual.com/web/.
    Args:
        sequence (list of str): List of flashing colors in order.
        vowel (bool): Whether the serial number contains a vowel.
        strikes (int): Current number of strikes (0-2).
    Returns:
        list of str: List of colors to press in order.
    """
    table = TABLE[vowel][strikes] # Select the correct mapping table
    return [table[color] for color in sequence] # Translate each color in the sequence

def main():
    print("=== SIMON SAYS (SEQUENTIAL) SOLVER ===")
    
    has_vowel = input("Does the serial number contain a vowel? (y/n): ").lower().startswith("y")
    strikes = int(input("Current strikes (0-2): ").strip())

    sequence = []

    print("\nEnter flashes one sequence at a time.")
    print("Example:")
    print("  First input: red")
    print("  Second input: red blue")
    print("  Third input: red blue yellow")
    print("Type 'q' to quit.\n")

    while True:
        flashes = input(f"Enter {len(sequence)+1} flashing colors (space-separated): ").strip().lower()

        if flashes == "q": # Quit condition
            break

        colors = flashes.split()

        # Ensure sequence grows correctly
        if len(colors) != len(sequence) + 1:
            print(f"You must enter exactly {len(sequence)+1} colors.")
            continue

        for c in colors:
            if c not in ("red", "blue", "green", "yellow"):
                print(f"Invalid color: {c}")  # Invalid color check
                break
        else:
            # Sequence is valid
            translated = translate_sequence(colors, has_vowel, strikes) 

            print("\nPRESS THIS SEQUENCE:")
            print(" ".join(color.upper() for color in translated))
            print("----------------------------")
            continue

        print("Try again.")

if __name__ == "__main__":
    main()
