# Exercise 8
# Problem: Use nested if statements to determine if a given number is positive, even, or odd.
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
    if num % 2 == 0:
        print("The number is also even.")
    else:
        print("The number is odd.")
else:
    print("The number is not positive.")
