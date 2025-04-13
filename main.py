import sys

from stats import count_words
from stats import count_each_character
from stats import sort_characters

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) != 2 or type(sys.argv[1]) != str:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text_relpath = sys.argv[1]
    print(f"Analyzing book found at {text_relpath}")
    book_text = get_book_text(text_relpath)
    print("----------- Word Count ----------")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    character_counts = count_each_character(book_text)
    sorted_list = sort_characters(character_counts)
    for char_dict in sorted_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["count"]}")

    print("============= END ===============")


main()