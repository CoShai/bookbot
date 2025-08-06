import sys

from stats import get_word_count
from stats import get_char_count
from stats import get_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath=sys.argv[1]
    text=get_book_text(filepath)
    count=get_word_count(text)
    char_count_dict=get_char_count(text)
    sorted_list=get_sorted_list(char_count_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    
    for char in sorted_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")
    
    
main()    