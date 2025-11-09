def solve_button(color, text, num_batteries, has_car, has_frk):
    """
    Determines which action(s) to take with the Button in the 'Button' module of Keep Talking and Nobody Explodes.
    All the logic is taken from the Manual at https://www.bombmanual.com/web/.

    Args:
        color (str): Color of the button.
        text (str): Text on the button.
        num_batteries (int): Number of batteries on the bomb.
        has_car (bool): Whether there is a lit CAR indicator on the bomb.
        has_frk (bool): Whether there is a lit FRK indicator on the bomb.

    Returns:
        str: Instruction on what to do with the button.
    """
    

    color, text = color.lower(), text.lower()

    if color == "blue" and text == "abort":
        return "Hold the button. (Check strip color.)"
    elif num_batteries > 1 and text == "detonate":
        return "Press and immediately release the button."
    elif color == "white" and has_car:
        return "Hold the button. (Check strip color.)"
    elif num_batteries > 2 and has_frk:
        return "Press and immediately release the button."
    elif color == "yellow":
        return "Hold the button. (Check strip color.)"
    elif color == "red" and text == "hold":
        return "Press and immediately release the button."
    else:
        return "Hold the button. (Check strip color.)"

def button_strip_rule(strip_color):
    """
    Given the color of the lit strip after holding the button, tells you when to release the button.
    All the logic is taken from the Manual at https://www.bombmanual.com/web/.

    Args:
        strip_color (str): Color of the lit strip.

    Returns:
        str: Instruction on when to release the button.
    """
    color = strip_color.lower()
    if color == "blue":
        return "Release when the countdown timer has a 4 in any position."
    elif color == "white":
        return "Release when the countdown timer has a 1 in any position."
    elif color == "yellow":
        return "Release when the countdown timer has a 5 in any position."
    else:
        return "Release when the countdown timer has a 1 in any position."

def main():
    print("=== BUTTON MODULE SOLVER ===")
    color = input("Button color: ")
    text = input("Button text: ")
    batteries = int(input("Number of batteries: "))
    has_car = input("Lit CAR indicator? (y/n): ").lower() == 'y'
    has_frk = input("Lit FRK indicator? (y/n): ").lower() == 'y'

    result = solve_button(color, text, batteries, has_car, has_frk)
    print("\n" + result)

    if "Hold" in result:
        strip = input("Enter strip color: ")
        print(button_strip_rule(strip))

if __name__ == "__main__":
    main()



