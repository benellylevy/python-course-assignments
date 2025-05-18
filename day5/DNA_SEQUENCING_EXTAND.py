# extended_dna_sequencing.py

def extract_valid_sequences(sequence):
    # אנחנו מגדירים את הנוקלאוטידים התקינים A, C, T, G
    valid_bases = "ACTG"
    valid_sequences = []
    current_sequence = ""

    # רצים על הרצף אות אות עד למפגש עם אות לא תקינה, שם אנחנו שומרים את הרצף ופותחים חדש.
    for char in sequence:
        if char in valid_bases:
            current_sequence += char
        else:
            if current_sequence:  # If a valid subsequence is found, add it to the list
                valid_sequences.append(current_sequence)
                current_sequence = ""  # Reset for a new subsequence

    if current_sequence:  # If there's a valid subsequence left after the loop, add it
        valid_sequences.append(current_sequence)

    return valid_sequences


def main():
    # Ask for the DNA sequence input from the user
    sequence = input("Please type in a sequence: ")

    # Get the valid subsequences
    valid_sequences = extract_valid_sequences(sequence)
    print(valid_sequences)

    # Sort the sequences by length in descending order
    valid_sequences.sort(key=len, reverse=True)

    # Output the sorted list
    print(valid_sequences)


if __name__ == '__main__':
    main()