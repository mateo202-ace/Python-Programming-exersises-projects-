def square_positive_numbers(numbers):
    result = []
    for num in numbers:
        if num > 0:
            squared = num ** 2
            result.append(squared)
    return result

numbers = [4, -1, 3, 0, 2, -5, 6]
print(square_positive_numbers(numbers))