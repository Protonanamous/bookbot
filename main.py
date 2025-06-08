import sys
from stats import get_num_words, char_freq

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("-----------Word Count -----------")
    
    get_num_words(sys.argv[1])
    
    print("---------Character Count --------")
    char_freq(sys.argv[1])

    
main()
