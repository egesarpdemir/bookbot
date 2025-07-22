# text input word counting
def count_words(text):
    words = text.split()
    num_words = 0
    for word in words:
        num_words += 1
    return num_words

# text input turned into dic of cha and num of cha

def text_to_cha(text):
    dic = {}
    for cha in text:
        lowered = cha.lower()
        if lowered in dic:
            dic[lowered] += 1
        else:
            dic[lowered] = 1
    return dic


def sort_on(d):
    return d["num"]


def dict_sort_list(num_chars_dict):
    sorted_list = []
    for cha in num_chars_dict:
        sorted_list.append({"char": cha, "num": num_chars_dict[cha]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list