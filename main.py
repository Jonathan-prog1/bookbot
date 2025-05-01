#!/usr/bin/python3
from stats import get_num_words,get_letters_count,get_sorted_char_list
import sys
def main():
    
    #Check if correct number of arguments are provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # Get the path from command line arguments
    path_to_book = sys.argv[1]

    #Start of BOOKBOT

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    print("----------- Word Count ----------")
    get_num_words(path_to_book)
    print("--------- Character Count -------")
    char_counts = get_letters_count(path_to_book)
    sorted_chars = get_sorted_char_list(char_counts)
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]

        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
main()
