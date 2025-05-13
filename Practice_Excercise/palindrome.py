def check_palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[-(i+1)]:
            return False
    return True


words = ["racecar", "hello", "madam", "world"]
for word in words:
    if check_palindrome(word):
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")
