import sys

if len(sys.argv) != 2:
    print("Usage: python circle.py <radius>")
    sys.exit(1)

try:
    radius = float(sys.argv[1])
    area = 3.14 * radius * radius
    circumference = 2 * 3.14 * radius   
    print("The area of the circle is: ", area)
    print("The circumference of the circle is: ", circumference)
except ValueError:
    print("Error: Please provide a valid number for the radius")
    sys.exit(1)