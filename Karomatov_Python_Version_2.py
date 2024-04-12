"""
Version 2 In this version I used If statement and did only what asked steps!
Task 1. Make up an algorithm
  If the entered number is greater than 7, then print “Hello”
  If the entered name matches “John”, then output “Hello, John”, if not, then output "There is no such name"
  There is a numeric array at the input, it is necessary to output array elements that are multiples of 3
"""

# Input from the user
user_input = input("Enter Number, Name or Array: (Note: If you want to enter array, please separate with comma.) >>> ")

# This will be used for collecting numbers which multiples of 3
multiples_of_3 = []

# Try to parse the input as a float
try:
    user_input_float = float(user_input)
except ValueError:
    user_input_float = None


# Try to parse the input as a list
try:
    if ',' in user_input:
        user_input_list = [float(item.strip()) for item in user_input.split(',')]
    else:
        user_input_list = eval(user_input)
        if not isinstance(user_input_list, list):
            user_input_list = None
except (NameError, SyntaxError):
    user_input_list = None


# Perform different actions based on the type of input
if isinstance(user_input_float, float):
    if user_input_float > 7:
        print("Hello")
    else:
        print("Not Greated than 7")


# checking list and multiples of 3
elif isinstance(user_input_list, list):
    print("Received Array:", user_input_list)
    for number in user_input_list:
        if number % 3 == 0:
            multiples_of_3.append(number)
    if multiples_of_3:
        print("Multiples of 3:", multiples_of_3)
    else:
        print("There is no number Which is divided by 3.")


# Checking name matches with John or not8
elif isinstance(user_input, str):
    if user_input.title() != "John":
        print("There is no such name.")
    else:
        print("Hello", user_input.title())
else:
    print("Unknown type")
