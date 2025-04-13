def count_words(text):
    words = text.split()
    return len(words)
def count_each_character(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
def get_count(single_dict):
    return single_dict["count"]
def sort_characters(char_count):
    list_of_chars = []
    for char in char_count:
        new_dict = {
            "char": char,
            "count": char_count[char]
        }
        list_of_chars.append(new_dict)
    list_of_chars.sort(reverse=True, key=get_count)
    return list_of_chars