import sys
from stats import get_num_words, get_each_character_count, print_character_count

def get_book_text(filepath):
    with open(filepath, "r") as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============= START ===============")
    book_text = get_book_text(sys.argv[1])
    print(f"Analyzing book found at {sys.argv[1]}")
    num_words = get_num_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    characters = get_each_character_count(book_text)
    print_character_count(characters)
    # print(characters)

    print("============= END ===============")

main()
