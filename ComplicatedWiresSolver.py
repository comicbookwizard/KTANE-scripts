def solve_complicated_wire(has_red, has_blue, has_star, led_on, last_digit_even, has_parallel, num_batteries):
    """
    Determines which wire to cut in the 'Complicated Wires' module of Keep Talking and Nobody Explodes.
    All the logic is taken from the Manual at https://www.bombmanual.com/web/.
    Args:
        has_red (bool): Whether the wire has red color.
        has_blue (bool): Whether the wire has blue color.
        has_star (bool): Whether the wire has a star symbol.
        led_on (bool): Whether the LED is on.
        last_digit_even (bool): Whether the last digit of the serial number is even.
        has_parallel (bool): Whether the bomb has a parallel port.
        num_batteries (int): Number of batteries on the bomb.
    Returns:
        str: Instruction on which wire to cut.
    """
    if has_red and has_blue:
        if led_on and has_star:
            return "Do NOT cut the wire."
        elif led_on and not has_star and last_digit_even:
            return "Cut the wire."
        elif not led_on and has_star and has_parallel:
            return "Cut the wire."
        elif not led_on and not has_star and last_digit_even:
            return "Cut the wire."
        else:
            return "Do NOT cut the wire."
    elif has_red:
        if led_on and num_batteries >= 2:
            return "Cut the wire."
        elif not led_on and has_star:
            return "Cut the wire."
        elif not led_on and not has_star and last_digit_even:
            return "Cut the wire."
        else:
            return "Do NOT cut the wire."
    elif has_blue:
        if led_on and has_parallel:
            return "Cut the wire."
        elif not led_on and has_star:
            return "Do NOT cut the wire."
        elif not led_on and not has_star and last_digit_even:
            return "Cut the wire."
        else:
            return "Do NOT cut the wire."
    else:
        if not led_on:
            return "Cut the wire."
        if led_on and has_star and num_batteries >= 2:
            return "Cut the wire."
        if led_on and not has_star:
            return "Do NOT cut the wire."
        else:
            return "Do NOT cut the wire."


def main():
    print("=== COMPLICATED WIRES SOLVER ===")
    red = input("Wire has red color? (y/n): ").lower() == 'y'
    blue = input("Wire has blue color? (y/n): ").lower() == 'y'
    star = input("Wire has star symbol? (y/n): ").lower() == 'y'
    led = input("LED is on? (y/n): ").lower() == 'y'
    even = input("Last digit of serial number even? (y/n): ").lower() == 'y'
    parallel = input("Bomb has parallel port? (y/n): ").lower() == 'y'
    batteries = int(input("Number of batteries: "))

    print("\n" + solve_complicated_wire(red, blue, star, led, even, parallel, batteries))


if __name__ == "__main__":
    main()
