def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    report_book(text, book_path)



def report_book(text, path):
    print(f"--- Begin report of {path} ---")

    print(f"{count_words(text)} words found in the document")

    print_sorted_dict(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def get_count_letters(text):
    char_dict = {}
    lowered_text = text.lower()
    for i in range(0, len(lowered_text)):
        char = lowered_text[i]
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict


def sort_on(char_dict):
    return char_dict["num"]


def print_sorted_dict(text):
    char_dict = get_count_letters(text)
    new_dict = []
    for char in char_dict:
        if char.isalpha():
            new_dict.append({"name": char, "num": char_dict[char]})

    new_dict.sort(reverse=True, key=sort_on)

    for entry in new_dict:
        print(f"The '{entry['name']}' character was found {entry['num']} times")


main()
