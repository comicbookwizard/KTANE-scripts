RED_RULES = { # Logic for red wires
    1: "C", 2: "B", 3: "A",
    4: "AC", 5: "B", 6: "AC",
    7: "ABC", 8: "AB", 9: "B"
}

BLUE_RULES = { # Logic for blue wires
    1: "B", 2: "AC", 3: "B",
    4: "A", 5: "B", 6: "BC",
    7: "C", 8: "AC", 9: "A"
}

BLACK_RULES = { # Logic for black wires
    1: "ABC", 2: "AC", 3: "B",
    4: "AC", 5: "B", 6: "BC",
    7: "AB", 8: "C", 9: "C"
}

def should_cut(color, occurrence, destination):
    """
    Determines which wires to cut in the 'Wire Panels' module of Keep Talking and Nobody Explodes.
    All the logic is taken from the Manual at https://www.bombmanual.com/web/.
    Args:
        color (str): Color of the wire ("red", "blue", "black").
        occurrence (int): The occurrence number of this color wire (1 for first, 2 for second, etc.).
        destination (str): The destination letter of the wire ("A", "B", "C").
    Returns:
        bool: True if the wire should be cut, False otherwise.
    """
    rules = {"red": RED_RULES, "blue": BLUE_RULES, "black": BLACK_RULES}[color] # Select rules based on color
    allowed = rules[occurrence] # Get allowed destinations for this occurrence
    return destination in allowed or allowed == "ABC" # Determine if we should cut the wire

def main():
    print("=== WIRE PANELS (SEQUENCES) SOLVER ===")
    print("Enter the wires for each panel all at once.")
    print("Format per wire:  color destination")
    print("Example: red C")
    print("Enter an empty line when finished with a panel.\n")

    red = blue = black = 0

    panel_number = 1

    while True:
        print(f"\n--- PANEL {panel_number} ---")
        print("Enter up to 3 wires. Leave blank line to finish panel.\n")

        wires = []

        # Collects up to 3 wires for the panel
        while len(wires) < 3:
            line = input(f"Wire {len(wires)+1}: ").strip()
            if line == "":
                break

            parts = line.split()
            if len(parts) != 2:
                print("Invalid format. Use: 'red C'")
                continue

            color, dest = parts
            color = color.lower()
            dest = dest.upper()

            if color not in ("red", "blue", "black") or dest not in "ABC":
                print("Invalid wire. Try again.")
                continue

            wires.append((color, dest))

        if not wires:
            print("No wires entered. Ending solver.")
            break

        print("\nRESULTS:")
        for color, dest in wires:
            # Increment occurrence counter
            if color == "red":
                red += 1
                occ = red
            elif color == "blue":
                blue += 1
                occ = blue
            else:
                black += 1
                occ = black

            cut = should_cut(color, occ, dest)
            action = "CUT" if cut else "DO NOT CUT"

            print(f"{color.upper()} wire to {dest}: {action}")

        panel_number += 1

        if input("\nNext panel? (y/n): ").lower().startswith("n"):
            break


if __name__ == "__main__":
    main()
