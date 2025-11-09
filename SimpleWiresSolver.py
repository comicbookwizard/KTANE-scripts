def solve_wires(wires, last_serial_digit):
    """
    Determines which wire to cut in the 'Wires' module of Keep Talking and Nobody Explodes.
    All the logic is taken from the Manual at https://www.bombmanual.com/web/.
    Args:
        wires (list of str): List of wire colors from top to bottom.
        last_serial_digit (int): Last digit of the bomb's serial number.
    Returns:
        str: Instruction on which wire to cut.
    """
    num_wires = len(wires) # Get the number of wires
    is_odd = last_serial_digit % 2 == 1 # Check if the last digit of the serial number is odd

    def ordinal(n): # Helper function to convert number to ordinal string, used for when you need to cut a wire that can be in multiple positions
        return {1: "1st", 2: "2nd", 3: "3rd"}.get(n, f"{n}th")

    # 3 wires
    if num_wires == 3:
        if 'red' not in wires:
            return "Cut the 2nd wire."
        elif wires[-1] == 'white':
            return "Cut the last wire."
        elif wires.count('blue') > 1:
            return f"Cut the {ordinal(len(wires) - wires[::-1].index('blue'))} wire (last blue wire)."
        else:
            return "Cut the last wire."

    # 4 wires
    elif num_wires == 4:
        if wires.count('red') > 1 and is_odd:
            return f"Cut the {ordinal(len(wires) - wires[::-1].index('red'))} wire (last red wire)."
        elif (wires[-1] == 'yellow' and 'red' not in wires) or wires.count('blue') == 1: # Combined conditions because they lead to the same action and are one after another in the manual
            return "Cut the 1st wire."
        elif wires.count('yellow') > 1:
            return "Cut the last wire."
        else:
            return "Cut the 2nd wire."

    # 5 wires
    elif num_wires == 5:
        if wires[-1] == 'black' and is_odd:
            return "Cut the 4th wire."
        elif wires.count('red') == 1 and wires.count('yellow') > 1:
            return "Cut the 1st wire."
        elif 'black' not in wires:
            return "Cut the 2nd wire."
        else:
            return "Cut the 1st wire."

    # 6 wires
    elif num_wires == 6:
        if 'yellow' not in wires and is_odd:
            return "Cut the 3rd wire."
        elif wires.count('yellow') == 1 and wires.count('white') > 1:
            return "Cut the 4th wire."
        elif 'red' not in wires:
            return "Cut the last wire."
        else:
            return "Cut the 4th wire."


def main():
    print("=== WIRES MODULE SOLVER ===")
    print("Enter wire colors from top to bottom (e.g. red blue white yellow).")
    
    colors = input("Wires: ").strip().lower().split()
    if not (3 <= len(colors) <= 6):
        print("Error: There must be between 3 and 6 wires.")
        return

    serial = input("Last digit of serial number: ")
    if not serial.isdigit() or not (0 <= int(serial) <= 9):
        print("Error: Serial number digit must be between 0 and 9.")
        return

    print("\nAnalyzing...\n")
    print(solve_wires(colors, serial))


if __name__ == "__main__":
    main()
