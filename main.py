from stats import get_num_words, characters_dictionare, get_book_content,sort_dict

def main():

    book = "books/frankenstein.txt"
    number_words = get_num_words(book)
    file_content = get_book_content("books/frankenstein.txt")
    char_dict = characters_dictionare(file_content)
    dictionary = sort_dict(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {number_words} total words")
    print("--------- Character Count -------")
    for letter in dictionary:
        char = letter["char"]
        num = letter["num"]
        print(f"{char}: {num}")

main()
    