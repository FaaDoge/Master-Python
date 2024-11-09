# Exercise 3
# Problem: Check if a character is a vowel or not.
char = input("Enter a single character: ").lower()
if char in 'aeiou':
    print(f"{char} is a vowel.")
else:
    print(f"{char} is not a vowel.")