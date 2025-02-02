def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)

    book_report(book_path, word_count, char_count)

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents
    
def get_word_count(text):
    word_count = len(text.split())
    return word_count

def get_char_count(text):
    character_count = {}
    lc_text = text.lower()

    for char in lc_text:
        if char in character_count.keys():
            character_count[char] += 1
        else:
            character_count[char] = 1

    return character_count

def book_report(book_path, word_count, char_count):
    print(f"--- Report of {book_path} ---")
    print(f"{word_count} words in the document")

    sorted_char_count = dict(sorted(char_count.items()))

    for key in sorted_char_count:
        if key.isalpha():
            print(f"The character '{key}' was found {sorted_char_count[key]} times")

    print("--- End of report ---")

main()
