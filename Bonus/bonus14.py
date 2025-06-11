from parsers14 import parse_input
from convertes14 import convert


feet_inches = input("Enter feet and inches: ")


(feet, inches) = parse_input(feet_inches)
if feet is not None and inches is not None:
    print(convert(feet, inches))
