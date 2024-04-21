def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(get_word_count(text))

def get_word_count(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_letter_count(text):
    pass

main()