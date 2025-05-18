#נעשה פונקציה שמקבלת רשימות של מספרים - עוברת עליהם אחד אחד - ומונה כמה פעמים מופיע מספר בודד בין 0-9, כל פעם שהוא מופיע מתווסף אחד לערך שלו במילון
def count_digits(numbers):
    # אני יוצר מילון לשמירה של המספרים 0-9
    digit_count = {str(i): 0 for i in range(10)}

    # Iterate through each number in the list
    for number in numbers:
        # Convert number to string to easily access individual digits
        for digit in str(abs(number)):  # abs() ensures that negative numbers are handled
            if digit.isdigit():  # Only count digits (ignore any other characters)
                digit_count[digit] += 1

    return digit_count


def main():
    # הדוגמה שצרפתה לאתר
    numbers = [1203, 1256, 312456, 98]

    # הפונקציה מקבלת את הערך numbers ומפעילה עליו את הפונקציה שבנינו ואז שומרת בערך digit
    digit_counts = count_digits(numbers)

    # Print the result
    print("Digit counts:")
    for digit, count in digit_counts.items():
        print(f"Digit {digit}: {count}")


if __name__ == '__main__':
    main()