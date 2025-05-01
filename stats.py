def get_book_text(path_to_file):
    with open(path_to_file) as b:
        file_contents = b.read()
        return file_contents

def get_num_words(path_to_file):
    
    words = get_book_text(path_to_file).split()

    num_words = len(words)

    print(f"Found {num_words} total words")
def get_letters_count(path_to_file):
    text = get_book_text(path_to_file)
    char_counts = {}

    for char in text:
        char = char.lower()

         # If character already exists in dictionary, increment its count
        if char in char_counts:
            char_counts[char] += 1
        # If it's a new character, add it to dictionary with count 1
        else:
            char_counts[char] = 1

    return char_counts

def get_sorted_char_list(char_counts):
    sorted_chars = []

    #add to sorted chars
    for char, count in char_counts.items():
        sorted_chars.append({"char": char, "num": count})

        def sort_on(dict):
            return dict["num"]

    # Sort the list in descending order (reverse=True)
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars
