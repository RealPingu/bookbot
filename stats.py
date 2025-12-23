def count_words(book_str):
    word_list = book_str.split()
    return len(word_list)    

def count_characters(book_str):
    char_dict = {}
    book_str = book_str.lower()
    for char in book_str:
        if char in char_dict:
            #if exist, just add 1
            char_dict[char] += 1
        else:
            #counts +1 as the first instance of a new char
            char_dict[char] = 1
    return char_dict


def sort_on(items):
    return items["num"]

def sorted_dict(unsorted_dict):
    sorted_list_dict = []
    for item in unsorted_dict:
        sorted_list_dict.append({"char":str(item), "num":unsorted_dict[item]})
    
    sorted_list_dict.sort(reverse=True, key=sort_on)
    
    return sorted_list_dict

def alpha_numeric(sorted_dict):
    for item in sorted_dict:
        if str(item["char"]).isalpha():
            print(f"{str(item["char"])}: {item["num"]}")