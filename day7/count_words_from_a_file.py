"""
Count the number of times each word appears in a text file,
and write the results into a new file called 'word_count.txt'.

This script is as unadorned and practical as a well-used hammer.
"""

from collections import Counter
import os

def count_words(input_filename):
    # Read the text file faithfully, stripping all but the essence.
    with open(input_filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    
    # Split text into words based on space.
    words = text.split()
    
    # Count each word, as a shepherd knows each sheep.
    word_counts = Counter(words)

    # Prepare the result fer saving.
    with open('word_count.txt', 'w', encoding='utf-8') as output_file:
        for word, count in word_counts.items():
            output_file.write(f"{word}: {count}\n")

if __name__ == "__main__":
    filename = input("Enter the path to the text file to count: ").strip()
    count_words(filename)
    base, ext = os.path.splitext(filename)
    output_filename = f"{base}_count.txt"
    print(f"Word count has been written to '{output_filename}'. Tradition endures.")
