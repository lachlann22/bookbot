# Gets and prints a report of the number of words and characters in a text
def main():
    # Define the text to use 
    book_path = "books/frankenstein.txt"

    # Get the text of the book into a string
    text = get_book_text(book_path)

    # Get a count of the number of discrete words
    word_count = book_word_count(text)

    # Get a count for the number of times each character is used
    character_count = get_character_count(text)

    # Take the word and character count and return a nice report
    get_book_report(book_path, word_count, character_count)
    

# Open the book and return the contents as a string
def get_book_text(path):
    with open(path) as f:
        return f.read()
    

# Count the number of words in a string, separating by whitespace   
def book_word_count(text_string):
    word_list = list(text_string.split())
    return len(word_list)


# Check each character in the string, and create a dictionary with char:count
def get_character_count(text_string):
    characters = {}
    lowered_string = text_string.lower()
    for c in lowered_string:
        if c.isalpha():
            if c in characters:
                characters[c] += 1
            else:
                characters[c] = 1
    return characters


# Print a report of the word and character count for the book
def get_book_report(path, words, chars):
    # Header of report
    print(f"*--- Begin report for {path} ---*")

    # Word count
    print(f"{words} found in the document.")

    # Character count
    for c in chars:
        print(f"The {c} character was found {chars[c]} times.")

main()