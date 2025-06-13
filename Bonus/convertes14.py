def convert(feet, inches):
    try:

        centimeters = (feet * 30.48) + (inches * 2.54)
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None

    return f"{feet} feet and {inches} inches is equal to {centimeters} centimeters."
