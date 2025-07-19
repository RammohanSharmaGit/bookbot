def get_character_count(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        char_dict[char] = char_dict.get(char,0) +1
    return char_dict

def get_word_count(text):
    split_words = text.split()
    split_words_count = len(split_words)
    print(f"Found {split_words_count} total words")        
