def find_duplicates(numbers):
    seen = set()
    duplicates = []

    for num in numbers:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        seen.add(num)

    return duplicates


numbers = [1, 2, 3, 4, 5, 1, 2, 6, 7, 2, 3, 8]
print(find_duplicates(numbers))
