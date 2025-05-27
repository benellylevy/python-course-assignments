import sys
import os


# for activate that function you will need to run from terminal with the text filr - you get the new one to the place the first one was with "root13" as the continiue name
def rot13(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += char
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python rot13_file.py <filename>")
        sys.exit(1)

    input_filename = sys.argv[1]

    if not os.path.isfile(input_filename):
        print(f"File '{input_filename}' does not exist.")
        sys.exit(1)

    with open(input_filename, "r", encoding="utf-8") as f:
        content = f.read()

    encoded_content = rot13(content)

    # יצירת שם קובץ חדש: <שםקובץ_מקורי>_מוצפן.txt
    name, ext = os.path.splitext(input_filename)
    output_filename = f"{name}root13.txt"

    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(encoded_content)

    print(f"Encrypted file saved as '{output_filename}'")