def main():
    print("--- Starting report of books/frankenstein.txt ---")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    # Count words and print the result
    word_count = word_number_counter(file_contents)
    print(f"{word_count} words found in the document")
    
    # Count character occurrences
    character_count = character_counter(file_contents)
    
    # Transform the character counts dictionary into a list of dictionaries
    char_list = [{"char": char, "num": count} for char, count in character_count.items()]
    
    # Sort the list by the number of occurrences
    char_list.sort(reverse=True, key=sort_on)
    
    # Print each character and its count (sorted)
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End of report ---")


def word_number_counter(text):
    words_in_text = text.split()
    return len(words_in_text)


def character_counter(text):
    char_counts = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in char_counts:
            char_counts[char] += 1
        elif char.isalpha():
            char_counts[char] = 1
    return char_counts


def sort_on(item):
    return item["num"]

main()
