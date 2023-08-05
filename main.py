def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = split_text(text)
    letter_frequency = get_letter_frequency(text)
    report = get_report(letter_frequency)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for letter, count in report:
        print(f"the '{letter}' character was found {count} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def split_text(text):
    words = text.split()
    return len(words)

def get_letter_frequency(text):
    character_list = list(text)
    character_dict = {}
    for i in character_list:
        char = i.lower()
        if char in character_dict:
            character_dict[char] += 1 
        else:
            character_dict[char] = 1
    return character_dict

def get_report(letter_frequency):
    letter_list = list(letter_frequency.items())
    letter_list.sort(key=lambda x: x[1], reverse=True)
    to_remove = []

    for i in letter_list:
        if i[0].isalpha() == False:
            to_remove.append(i)

    for i in to_remove:
        letter_list.remove(i)
    
    return letter_list





main()
