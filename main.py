import sys
from stats import get_word_count , get_character_count

def get_book_text(filePath):
    with open(filePath) as f:
        return f.read()
    
def sort_on(dict):
    return dict["num"]

def print_report(sorted_dict_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    get_word_count(get_book_text(sys.argv[1]))
    print("--------- Character Count -------")
    for dict in sorted_dict_list:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")    

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    char_dict = get_character_count(get_book_text(sys.argv[1]))
    sorted_dict_list = []
    for key in char_dict:
        if (key.isalpha()):
            current_dict = {"char": key, "num": char_dict[key]}
            sorted_dict_list.append(current_dict)
    sorted_dict_list.sort(key = sort_on, reverse= True)
    print_report(sorted_dict_list)

main()