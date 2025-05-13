def bubble_sort(numbers):
    n = len(numbers) # gets the len of the list
    for i in range(n): # outer loop, runs n times for each element in the list
        for j in range(0, n - i - 1): # inner loop, make sure that the loop iterates 1 less each time it goes through
            if numbers[j] > numbers[j + 1]: # if number is greater than the number adjacent
                # swap the elements
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j] # if the number is greater it swaps it 
    return numbers


print(bubble_sort([45, 64, 34, 25, 12, 22, 11, 90]))
