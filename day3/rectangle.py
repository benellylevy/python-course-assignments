
import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python rectangle.py <height> <width>")
    sys.exit(1)

try:
    high = float(sys.argv[1])
    width = float(sys.argv[2])
    area = high * width
    perimeter = 2 * (high + width)
    print("The area of the rectangle is: ", area)   
    print("The perimeter of the rectangle is: ", perimeter)
except ValueError:
    print("Error: Height and width must be numeric values")
    sys.exit(1)