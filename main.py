from stats import (count_words, 
                   count_characters, 
                   sorted_dict, 
                   alpha_numeric)
import sys

def get_book_text(file_path):
    with open(file_path, encoding="utf-8-sig") as f:
        file_contents = f.read()
        return file_contents
       
def main():

    if len(sys.argv) < 2:
        print(f'Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        path_argument = sys.argv[1]
        amount_words = count_words(get_book_text(path_argument))
        char_count = count_characters(get_book_text(path_argument))

        sorted_list_dict = sorted_dict(char_count)

        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {amount_words} total words")
        print("--------- Character Count -------")
        alpha_numeric(sorted_list_dict)
        (f'============= END ===============')
    
        #print(sys.argv)
        
    
    
    
main()
