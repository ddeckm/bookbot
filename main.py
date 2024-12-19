def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    char_list = sorted_character_count(char_count)

    print(f"---Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in char_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was fount {item['num']} time")
    print("--- End report ---")

def get_book_text(path):
        with open(path) as f:
            return f.read()
       
def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char = {}
    for letter in text:
        letters = letter.lower()
        if letters in char:
            char[letters] += 1
        else:
            char[letters] = 1
    return char

def sort_on(d):
    return d["num"]

def sorted_character_count(text):
    char_dict = get_char_count(text)
    char_list = []
    for d in char_dict:
        char_list.append({"char": d, "num": text[d]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

    

main()