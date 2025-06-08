def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(filepath):

    num = 0
    text = get_book_text(filepath)
    for i in text.split():
        num += 1
    print(f"Found {num} total words")

def char_freq(filepath):
    count = 0
    char_dict = {}
    list_dict = []
    text = get_book_text(filepath).lower()
    for i in text:
        if i.isalpha():
            if i in char_dict:
                char_dict[i] = char_dict[i] + 1
            else:
                char_dict[i] = 1
    for i in char_dict:
        list_dict.append({"name": i, "num": char_dict[i]})
    list_dict.sort(reverse=True, key=sort_on)
    
    for i in list_dict:
        
        print(f"{list_dict[count]['name']}: {list_dict[count]['num']}")
        count += 1


# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]


