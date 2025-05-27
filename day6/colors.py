import sys
import os

def load_colors(filename):
    if not os.path.isfile(filename):
        print(f"Error: '{filename}' not found.")
        sys.exit(1)
    with open(filename, "r", encoding="utf-8") as f:
        # Remove empty lines and strip whitespace
        colors = [line.strip() for line in f if line.strip()]
    if not colors:
        print("Error: No colors found in the file.")
        sys.exit(1)
    return colors

def print_menu(colors):
    print("Select a color:")
    for idx, color in enumerate(colors, 1):
        print(f"{idx}. {color}")

def get_color_by_number(colors, number_str):
    try:
        number = int(number_str)
        if 1 <= number <= len(colors):
            return colors[number - 1]
        else:
            print(f"Error: Number must be between 1 and {len(colors)}.")
            return None
    except ValueError:
        print("Error: Please enter a whole number.")
        return None

def get_color_by_name(colors, name):
    for color in colors:
        if color.lower() == name.lower():
            return color
    print("Error: Color not found.")
    return None

def main():
    colors = load_colors("colors.txt")
    selected_color = None

    # Command line argument provided?
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        # Try as number
        color = get_color_by_number(colors, arg)
        if color:
            selected_color = color
        else:
            # Try as color name
            color = get_color_by_name(colors, arg)
            if color:
                selected_color = color
            else:
                print_menu(colors)
                return
    else:
        print_menu(colors)
        while selected_color is None:
            user_input = input("Enter the number of your color choice: ").strip()
            color = get_color_by_number(colors, user_input)
            if color:
                selected_color = color

    print(f"You selected: {selected_color}")

if __name__ == "__main__":
    main()