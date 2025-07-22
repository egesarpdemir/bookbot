import sys
from stats import text_to_cha, count_words, dict_sort_list

# file to string
def get_book_text(path):
    with open(path) as f:
        return f.read()


# main func  
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookpath = sys.argv[1]
    text = get_book_text(bookpath)
    num_words = count_words(text)
    characters = text_to_cha(text)
    cha_list = dict_sort_list(characters)
    
    
    print_report(bookpath, num_words, cha_list)

def print_report(bookpath, num_words, cha_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in cha_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()

