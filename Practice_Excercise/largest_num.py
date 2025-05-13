def find_largest(number):
    largest = number[0] #assume the first number is the largest
    for n in number:
        if n > largest:
            largest = n
    return largest

print(find_largest([2,6,12,43,566,232,21,98]))