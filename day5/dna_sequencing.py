# dna_sequencing.py
import sys

def extract_valid_sequences(sequence):
    # אנו מסננים רק את הבסיסים התקניים A, C, T, G, ומתעלמים רק מה-X
    valid_bases = "ACTG"
    valid_sequences = []
    current_sequence = ""

    for char in sequence:
        if char == 'X':  # אם התו הוא 'X', נתחיל רצף חדש
            if current_sequence:
                valid_sequences.append(current_sequence)
                current_sequence = ""  # נתחיל רצף חדש
        elif char.isalpha() and char in valid_bases:  # אם התו הוא אות תקנית A, C, T, G
            current_sequence += char
        elif not char.isalpha():  # אם לא מדובר באותיות, נתעלם מהן
            continue

    if current_sequence:  # נוסיף את הרצף האחרון אם יש
        valid_sequences.append(current_sequence)

    return valid_sequences

def main():
    if len(sys.argv) != 2:
        print("Usage: python dna_sequencing.py <sequence>")
        sys.exit(1)

    sequence = sys.argv[1]

    # שלב 1: חיתוך הרצפים התקניים
    valid_sequences = extract_valid_sequences(sequence)
    print(valid_sequences)
    # שלב 2: מיון לפי אורך
    valid_sequences.sort(key=len, reverse=True)

    print(valid_sequences)

if __name__ == '__main__':
    main()