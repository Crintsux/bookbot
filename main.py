def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(f"The word count is: {get_word_count(text)}")
    #print(get_char_count(text))
    print_report(text, book_path)
    
# returns number of words(int) in the input text
def get_word_count(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

# returns a text string from the input path
def get_book_text(path):
    with open(path) as f:
        return f.read()

# returns a dictionary where each key is a character
# found in the text and it's value is the number of
# times it was found in the text
def get_char_count(text):
    lowered_text = text.lower()
    output_dict = {}
    for char in lowered_text:
        if char not in output_dict:
            output_dict[char] = 1
        else:
            output_dict[char] += 1
    return output_dict

# returns values of dictionary keys
def get_value(dict):
    return dict["num"]

# prints a report containing the path to the text source,
# word count and a count of each letter sorted from the
# highest to the lowest occurence
def print_report(text, book):
    dict = get_char_count(text)
    character_list = []
    for item in dict:
        if item.isalpha():
            temp_dict = {}
            temp_dict["character"] = item
            temp_dict["num"] = dict[item]
            character_list.append(temp_dict)
    character_list.sort(reverse=True, key=get_value)
    print(f"--- Begin report of {book} ---")
    print(f"{get_word_count(text)} words were found in the document")
    for rec in character_list:
        print(f"The '{rec["character"]}' character was found {rec["num"]} times")
main()