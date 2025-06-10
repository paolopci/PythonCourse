
feet_inches = input("Enter feet and inches: ")


def parse_input(feet_inches):
    try:
        parts = feet_inches.split(' ')
        if len(parts) != 2:
            raise ValueError("Input must be in 'feet inches' format.")
        feet = float(parts[0])
        inches = float(parts[1])
        if feet < 0 or inches < 0:
            raise ValueError("Feet and inches must be non-negative.")
        if inches >= 12:
            raise ValueError("Inches must be less than 12.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None, None

    return (feet, inches)


def convert(feet, inches):
    try:

        centimeters = (feet * 30.48) + (inches * 2.54)
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None

    return f"{feet} feet and {inches} inches is equal to {centimeters} centimeters."


(feet, inches) = parse_input(feet_inches)
if feet is not None and inches is not None:
    print(convert(feet, inches))
