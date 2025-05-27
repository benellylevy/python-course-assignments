import sys
import os

def count_digits(filename):
    digit_counts = {str(i): 0 for i in range(10)}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            for char in line:
                if char in digit_counts:
                    digit_counts[char] += 1
    return digit_counts

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python count_digits_file.py <input_filename>")
        sys.exit(1)

    input_filename = sys.argv[1]

    if not os.path.isfile(input_filename):
        print(f"File '{input_filename}' does not exist.")
        sys.exit(1)

    counts = count_digits(input_filename)

    with open("report.txt", "w", encoding="utf-8") as f:
        for digit in range(10):
            f.write(f"{digit} {counts[str(digit)]}\n")

    print("Digit count report saved as 'report.txt'")