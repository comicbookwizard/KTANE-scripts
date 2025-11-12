def solve_memory():
    """
    Determines which buttons to press in the 'Memory' module of Keep Talking and Nobody Explodes.
    All the logic is taken from the Manual at https://www.bombmanual.com/web/.
    
    Returns:
        str: Instruction on which wire to cut.
    """

    print("=== MEMORY MODULE SOLVER ===")
    print("Follow the prompts for each stage.")

    positions = {}
    labels = {}

    for stage in range(1, 6):
        print(f"\n--- Stage {stage} ---")
        display = int(input("Display number (1-4): "))
        buttons = list(map(int, input("Button labels (e.g. 1 4 2 3): ").split()))
        if len(buttons) != 4:
            print("Invalid input. Must be exactly 4 numbers.")
            return

        if stage == 1:
            pos = [2, 2, 3, 4][display - 1]
        elif stage == 2:
            if display == 1:
                lbl = 4
                pos = buttons.index(lbl) + 1
            elif display == 2:
                pos = positions[1]
            elif display == 3:
                pos = 1
            else:
                pos = positions[1]
        elif stage == 3:
            if display == 1:
                lbl = labels[2]
                pos = buttons.index(lbl) + 1
            elif display == 2:
                lbl = labels[1]
                pos = buttons.index(lbl) + 1
            elif display == 3:
                pos = 3
            else:
                lbl = 4
                pos = buttons.index(lbl) + 1
        elif stage == 4:
            if display == 1:
                pos = positions[1]
            elif display == 2:
                pos = 1
            else:
                pos = positions[2]
        elif stage == 5:
            if display == 1:
                lbl = labels[1]
            elif display == 2:
                lbl = labels[2]
            elif display == 3:
                lbl = labels[4]
            else:
                lbl = labels[3]
            pos = buttons.index(lbl) + 1

        lbl = buttons[pos - 1]
        positions[stage] = pos
        labels[stage] = lbl

        print(f"→ Press the button in position {pos} (label {lbl}).")

if __name__ == "__main__":
    solve_memory()
