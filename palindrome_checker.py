def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

word = input("Enter word: ")

if is_palindrome(word):
    print("Palindrome")
else:
    print("Not palindrome")
