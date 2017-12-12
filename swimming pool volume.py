print("Throughout this program please use consistent units of measure.")

unitOfMeasure = input("Please enter your unit of measure: ").strip()

print("You do not need to enter the units of measure when asked for measurements.")

try:
    width = float(input("Width of Pool: "))
except ValueError:
    print("That is not a valid number!")
    raise SystemExit

try:
    length = float(input("Length of Pool: "))
except ValueError:
    print("That is not a valid number!")
    raise SystemExit

try:
    depth = float(input("Depth of Pool: "))
except ValueError:
    print("That is not a valid number!")
    raise SystemExit

volume = width * length * depth
surfaceArea = (width * length * 2) + (length * depth * 2) + (width * depth * 2)

try: # Try to use the ² character
    print("Volume of Pool: " + str(volume) + " " + unitOfMeasure + u"\u00B2")
except UnicodeEncodeError: # If output doesn't support Unicode then just use ^2
    print("Volume of Pool: " + str(volume) + " " + unitOfMeasure + "^2")
