import sys

from stats import count_words_in_text
from stats import count_characters_in_text
from stats import display_sorted_characters

def get_book_text(filepath):
    with open(filepath, "r") as file:
        return file.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words_in_text(text)
    char_count = count_characters_in_text(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words.")

    print("--------- Character Count -------")
    display_sorted_characters(char_count)

    print("============= END ===============")


if __name__ == "__main__":
    main()
