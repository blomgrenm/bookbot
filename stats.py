def get_book_content(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return len(file_contents.split())

def characters_dictionare(text_to_count):
    lower_version = text_to_count.lower()
    dictionary = {}
    for char in lower_version:
        if not char in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] += 1
    
    return dictionary

def sort_dict(dictionary):
    dict_list = []

    def sort_on(dict):
        return dict["num"]
    
    for i in dictionary:
        temp = {"char":i,"num":dictionary[i]}
        dict_list.append(temp)
    
    dict_list.sort(reverse=True,key=sort_on)

    return dict_list