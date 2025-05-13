from re import I
from unittest import result


def filter_strings(strings):
    result = []
    for string in strings:
        if len(string) > 3 and string[0].lower() in ('a', 'e', 'i', 'o', 'u'):
            result.append(string)
    return result

strings = ['apple', 'banana', 'kiwi', 'orange', 'a', 'egg', 'I', 'pie']
print(filter_strings(strings))


