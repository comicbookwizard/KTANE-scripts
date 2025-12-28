import os
import sys
from colorama import init, Fore

init(autoreset=True)

# UTILITY FUNCTIONS
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input(Fore.RED + "\nPress ENTER to return to the main menu...")

def title(text):
    print(Fore.RED + "=" * 50)
    print(Fore.RED + text)
    print(Fore.RED + "=" * 50 + "\n")


# SIMPLE WIRES FUNCTIONS
def solve_wires(wires, last_serial_digit):
    """
    Solves the simple wires module.
    
    Args:
        wires (list of str): List of wire colors from top to bottom.
        last_serial_digit (int): The last digit of the bomb's serial number.

    Returns:
        str: Instruction on which wire to cut.
    """
    num_wires = len(wires)
    is_odd = last_serial_digit % 2 == 1

    def ordinal(n):
        return {1:"1st",2:"2nd",3:"3rd"}.get(n, f"{n}th")

    if num_wires == 3:
        if 'red' not in wires:
            return "Cut the 2nd wire."
        elif wires[-1] == 'white':
            return "Cut the last wire."
        elif wires.count('blue') > 1:
            return f"Cut the {ordinal(len(wires) - wires[::-1].index('blue'))} wire (last blue)."
        else:
            return "Cut the last wire."

    elif num_wires == 4:
        if wires.count('red') > 1 and is_odd:
            return f"Cut the {ordinal(len(wires) - wires[::-1].index('red'))} wire (last red)."
        elif (wires[-1]=='yellow' and 'red' not in wires) or wires.count('blue') == 1:
            return "Cut the 1st wire."
        elif wires.count('yellow') > 1:
            return "Cut the last wire."
        else:
            return "Cut the 2nd wire."

    elif num_wires == 5:
        if wires[-1] == 'black' and is_odd:
            return "Cut the 4th wire."
        elif wires.count('red') == 1 and wires.count('yellow')>1:
            return "Cut the 1st wire."
        elif 'black' not in wires:
            return "Cut the 2nd wire."
        else:
            return "Cut the 1st wire."

    elif num_wires == 6:
        if 'yellow' not in wires and is_odd:
            return "Cut the 3rd wire."
        elif wires.count('yellow') == 1 and wires.count('white') > 1:
            return "Cut the 4th wire."
        elif 'red' not in wires:
            return "Cut the last wire."
        else:
            return "Cut the 4th wire."

def run_simple_wires():
    """Runs the simple wires module solver."""
    clear_screen()
    title("SIMPLE WIRES")

    try:
        colors = input("Wire colors (top to bottom): ").lower().split()
        if len(colors) < 3 or len(colors) > 6:
            raise ValueError("Number of wires must be between 3 and 6.")
        if any(c not in ("red","blue","white","yellow","black") for c in colors):
            raise ValueError("Invalid wire color detected.")
        
        serial = input("Last serial digit: ")
        if not serial.isdigit():
            raise ValueError("Last serial digit must be a number.")
        serial_int = int(serial)
        if serial_int < 0 or serial_int > 9:
            raise ValueError("Last serial digit must be between 0 and 9.")

        result = solve_wires(colors, serial_int)
        print(Fore.GREEN + "\n" + result)
    except ValueError as e:
        print(Fore.RED + f"Error: {e}")
    except Exception as e:
        print(Fore.RED + f"Unexpected error: {e}")
    finally:
        pause()


# BUTTON FUNCTIONS
def solve_button(color, text, num_batteries, has_car, has_frk):
    """
    Solves the button module.

    Args:
        color (str): Color of the button.
        text (str): Text on the button.
        num_batteries (int): Number of batteries on the bomb.
        has_car (bool): Whether there is a lit CAR indicator.
        has_frk (bool): Whether there is a lit FRK indicator.

    Returns:
        str: Instruction on how to handle the button.
    """
    color = color.lower()
    text = text.lower()

    if color == "blue" and text == "abort":
        return "Hold the button."
    elif num_batteries > 1 and text == "detonate":
        return "Press and release."
    elif color == "white" and has_car:
        return "Hold the button."
    elif num_batteries > 2 and has_frk:
        return "Press and release."
    elif color == "yellow":
        return "Hold the button."
    elif color == "red" and text == "hold":
        return "Press and release."
    else:
        return "Hold the button."

def strip_rule(strip):
    """
    Handles the strip color rules when holding the button.
    
    Args:
        strip (str): Color of the strip.
    
    Returns:
        str: Instruction on when to release the button.
    """
    strip = strip.lower()
    if strip == "blue":
        return "Release when timer has a 4."
    elif strip == "white":
        return "Release when timer has a 1."
    elif strip == "yellow":
        return "Release when timer has a 5."
    else:
        return "Release when timer has a 1."

def run_button():
    """Runs the button module solver."""
    clear_screen()
    title("BUTTON")

    colors = ["blue", "white", "yellow", "red", "black"]
    texts = ["abort", "detonate", "hold", "press"]
    strip_colors = ["blue", "white", "yellow", "red"]

    try:
        color = input("Button color: ")
        if color not in colors:
            raise ValueError("Invalid color.")
        
        text = input("Text on button: ")
        if text not in texts:
            raise ValueError("Invalid text.")
        
        bat_input = input("Number of batteries: ")
        try:
            bat = int(bat_input)
            if bat < 0:
                raise ValueError("Number of batteries must be non-negative.")
        except ValueError:
            raise ValueError("Invalid input for number of batteries.")
        
        car_in = input("Lit CAR indicator? (y/n): ").lower()
        if car_in not in ("y", "n"):
            raise ValueError("Invalid input for CAR indicator.")
        car = car_in == "y"
        
        frk_in = input("Lit FRK indicator? (y/n): ").lower()
        if frk_in not in ("y", "n"):
            raise ValueError("Invalid input for FRK indicator.")
        frk = frk_in == "y"
        
        result = solve_button(color, text, bat, car, frk)
        print(Fore.GREEN + "\n" + result)

        if "Hold" in result:
            strip = input("\nStrip color: ")
            if strip not in strip_colors:
                raise ValueError("Invalid strip color.")
            print(Fore.GREEN + strip_rule(strip))
    except ValueError as e:
        print(Fore.RED + f"Error: {e}")
    except Exception as e:
        print(Fore.RED + f"Unexpected error: {e}")
    finally:
        pause()


# COMPLICATED WIRES FUNCTIONS
# To-do: Add function to do another wire without returning to main menu
def solve_complicated_wires(red, blue, star, led, even, parallel, bat):
    """
    Solves the complicated wires module.

    Args:
        red (bool): Whether the wire contains red.
        blue (bool): Whether the wire contains blue.
        star (bool): Whether there is a star symbol.
        led (bool): Whether the LED is lit.
        even (bool): Whether the last digit of the serial number is even.
        parallel (bool): Whether the bomb has a parallel port.
        bat (int): Number of batteries on the bomb.
    """
    if red and blue:
        if led and star: 
            return "DO NOT CUT."
        if led and not star and even: 
            return "CUT."
        if not led and star and parallel: 
            return "CUT."
        if not led and not star and even: 
            return "CUT."
        return "DO NOT CUT."
    elif red:
        if led and bat >= 2: 
            return "CUT."
        if not led and star: 
            return "CUT."
        if not led and not star and even: 
            return "CUT."
        return "DO NOT CUT."
    elif blue:
        if led and parallel: 
            return "CUT."
        if not led and star: 
            return "DO NOT CUT."
        if not led and not star and even: 
            return "CUT."
        return "DO NOT CUT."
    else:
        if not led: 
            return "CUT."
        if led and star and bat >= 2: 
            return "CUT."
        if led and not star: 
            return "DO NOT CUT."
        return "DO NOT CUT."

def run_complicated_wires():
    """Runs the complicated wires module solver."""
    clear_screen()
    title("COMPLICATED WIRES")

    try:
        r_in = input("Has red? (y/n): ")
        if r_in not in ("y", "n"):
            raise ValueError("Invalid input for red wire.")
        red = r_in == "y"
        
        b_in = input("Has blue? (y/n): ")
        if b_in not in ("y", "n"):
            raise ValueError("Invalid input for blue wire.")
        blue = b_in == "y"
        
        s_in = input("Has star? (y/n): ")
        if s_in not in ("y", "n"):
            raise ValueError("Invalid input for star.")
        star = s_in == "y"
        
        l_in = input("LED lit? (y/n): ")
        if l_in not in ("y", "n"):
            raise ValueError("Invalid input for LED.")
        led = l_in == "y"

        e_in = input("Is the last digit of the serial number even? (y/n): ")
        if e_in not in ("y", "n"):
            raise ValueError("Invalid input for serial number digit.")
        even = e_in == "y"

        p_in = input("Does the bomb have a parallel port? (y/n): ")
        if p_in not in ("y", "n"):
            raise ValueError("Invalid input for parallel port.")
        parallel = p_in == "y"

        try:
            bat = int(input("Number of batteries: "))
            if bat < 0:
                raise ValueError("Number of batteries must be non-negative.")
        except ValueError:
            raise ValueError("Invalid input for number of batteries.")

        print(Fore.GREEN + "\n" + solve_complicated_wires(red, blue, star, led, even, parallel, bat))
    except ValueError as e:
        print(Fore.RED + f"Error: {e}")
    except Exception as e:
        print(Fore.RED + f"Unexpected error: {e}")
    finally:
        pause()


# MEMORY FUNCTIONS
def run_memory():
    """Runs the memory module solver."""
    clear_screen()
    title("MEMORY")

    positions = {}
    labels = {}

    try:
        for stage in range(1,6):
            print(Fore.YELLOW + f"\n-- Stage {stage} --")
            
            display = input("Display: ")
            if display not in ("1","2","3","4"):
                raise ValueError("Display must be between 1 and 4.")
            
            raw = input("Labels: ").strip().split()
            if len(raw) != 4:
                raise ValueError("Enter exactly 4 labels.")
            if not all(token.isdigit() for token in raw):
                raise ValueError("All labels must be numbers.")
            try:
                buttons = list(map(int, raw))
            except ValueError:
                raise ValueError("All labels must be numbers.")
            if any(not (1 <= b <= 4) for b in buttons):
                raise ValueError("Labels must be between 1 and 4.")

            if stage == 1:
                pos = [2,2,3,4][int(display)-1]
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
                    pos = buttons.index(lbl) +1
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
            else:
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

            print(Fore.GREEN + f"Press position {pos} (label {lbl}).")
    except ValueError as e:
        print(Fore.RED + f"Error: {e}")
    except KeyError as e:
        print(Fore.RED + f"Error: Missing required data from previous stage: {e}")
    except Exception as e:
        print(Fore.RED + f"Unexpected error: {e}")
    finally:
        pause()


# PASSWORDS FUNCTIONS


def run_password():
    """Runs the passwords module solver."""
    
    PASSWORD_WORDS = [
    "about","after","again","below","could","every","first","found","great","house",
    "large","learn","never","other","place","plant","point","right","small","sound",
    "spell","still","study","their","there","these","thing","think","three","water",
    "where","which","world","would","write"
    ]

    clear_screen()
    title("PASSWORDS")

    possible = PASSWORD_WORDS.copy()
    for i in range(5):
        letters = input(f"Column {i+1} letters: ").strip().lower()
        possible = [w for w in possible if w[i] in letters]

        print(Fore.CYAN + "Possible:", ", ".join(possible))

        if len(possible)==1:
            print(Fore.GREEN + "\nPASSWORD:", possible[0].upper())
            break

    pause()


# SIMON SAYS FUNCTIONS
TABLE = {
    True: {
        0: {"red":"blue","blue":"red","green":"yellow","yellow":"green"},
        1: {"red":"yellow","blue":"green","green":"blue","yellow":"red"},
        2: {"red":"green","blue":"red","green":"yellow","yellow":"blue"},
    },
    False:{
        0: {"red":"blue","blue":"yellow","green":"green","yellow":"red"},
        1: {"red":"red","blue":"blue","green":"yellow","yellow":"green"},
        2: {"red":"yellow","blue":"green","green":"blue","yellow":"red"},
    }
}

def run_simon():
    clear_screen()
    title("SIMON SAYS")

    try:
        vowel = input("Serial has vowel? (y/n): ").lower()=="y"
        try:
            strikes = int(input("Strikes (0-2): "))
            if strikes < 0 or strikes > 2:
                raise ValueError("Strikes must be between 0 and 2.")
        except ValueError:
            raise ValueError("Strikes must be a number between 0 and 2.")

        sequence = []
        while True:
            flashes = input(f"\nEnter {len(sequence)+1} flashes (or 'q'): ").lower().strip()
            if flashes == "q":
                break

            colors = flashes.split()
            if len(colors) != len(sequence)+1:
                print(Fore.RED + "Incorrect length.")
                continue

            sequence = colors
            try:
                translated = [TABLE[vowel][strikes][c] for c in sequence]
            except KeyError as e:
                print(Fore.RED + f"Error: Invalid color '{e}'. Use red, blue, green, or yellow.")
                continue

            print(Fore.GREEN + "PRESS:", " ".join(translated).upper())
    except ValueError as e:
        print(Fore.RED + f"Error: {e}")
    except Exception as e:
        print(Fore.RED + f"Unexpected error: {e}")
    finally:
        pause()


# WIRE SEQUENCES FUNCTIONS
RED_RULES   = {1:"C",2:"B",3:"A",4:"AC",5:"B",6:"AC",7:"ABC",8:"AB",9:"B"}
BLUE_RULES  = {1:"B",2:"AC",3:"B",4:"A",5:"B",6:"BC",7:"C",8:"AC",9:"A"}
BLACK_RULES = {1:"ABC",2:"AC",3:"B",4:"AC",5:"B",6:"BC",7:"AB",8:"C",9:"C"}

def should_cut(color, occ, dest):
    try:
        table = {"red":RED_RULES,"blue":BLUE_RULES,"black":BLACK_RULES}[color]
        if occ not in table:
            raise KeyError(f"Occurrence {occ} not found for color {color}")
        return dest in table[occ] or table[occ]=="ABC"
    except KeyError:
        raise

def run_wire_sequences():
    clear_screen()
    title("WIRE SEQUENCES")

    red = blue = black = 0

    try:
        while True:
            print(Fore.YELLOW + "\n--- New Panel ---")
            wires = []

            while len(wires)<3:
                line = input("Wire (e.g. 'red C') or blank: ").strip()
                if line == "":
                    break
                try:
                    color, dest = line.split()
                    if color.lower() not in ("red", "blue", "black"):
                        raise ValueError(f"Invalid color '{color}'. Use red, blue, or black.")
                    if dest.upper() not in ("A", "B", "C"):
                        raise ValueError(f"Invalid destination '{dest}'. Use A, B, or C.")
                    wires.append((color.lower(), dest.upper()))
                except ValueError as e:
                    print(Fore.RED + f"Error: {e}")
                    continue
                except Exception:
                    print(Fore.RED + "Error: Invalid format. Use 'color destination' (e.g. 'red C').")
                    continue

            if not wires:
                break

            print(Fore.CYAN + "\nRESULTS:")
            for color, dest in wires:
                try:
                    if color=="red":
                        red+=1; occ=red
                    elif color=="blue":
                        blue+=1; occ=blue
                    else:
                        black+=1; occ=black

                    result = should_cut(color, occ, dest)
                    print(
                        Fore.GREEN + f"{color.upper()} → {dest}: CUT"
                        if result else
                        Fore.RED + f"{color.upper()} → {dest}: DO NOT CUT"
                    )
                except KeyError as e:
                    print(Fore.RED + f"Error: Invalid color or destination: {e}")
                    continue

            if input("\nNext panel? (y/n): ")=="n":
                break
    except Exception as e:
        print(Fore.RED + f"Unexpected error: {e}")
    finally:
        pause()


# MAIN MENU FUNCTIONS
def main():
    while True:
        clear_screen()
        title("KTaNE MULTI-MODULE SOLVER")

        print(Fore.RED + "Choose a module:\n")
        print("1) Simple Wires")
        print("2) Button")
        print("3) Complicated Wires")
        print("4) Memory")
        print("5) Passwords")
        print("6) Simon Says")
        print("7) Wire Sequences")
        print("0) Exit\n")

        choice = input(Fore.RED + "Selection: ")

        if   choice=="1": run_simple_wires()
        elif choice=="2": run_button()
        elif choice=="3": run_complicated_wires()
        elif choice=="4": run_memory()
        elif choice=="5": run_password()
        elif choice=="6": run_simon()
        elif choice=="7": run_wire_sequences()
        elif choice=="0":
            clear_screen()
            print(Fore.GREEN + "Good luck defusing!")
            sys.exit()
        else:
            print(Fore.RED + "Invalid option.")
            pause()


if __name__ == "__main__":
    main()
