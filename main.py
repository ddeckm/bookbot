def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    print(char_count)

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

main()