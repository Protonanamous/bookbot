def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_num_words():

    num = 0
    text = get_book_text("/home/gg/bootdev/bookbot/books/frankenstein.txt")
    for i in text.split():
        num += 1
    print(f"{num} words found in the document")
