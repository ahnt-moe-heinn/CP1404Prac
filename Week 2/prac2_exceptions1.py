"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0


while not finished:
    try:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        result = first_number + second_number
        # TODO: this line
        # TODO: this line
        print("Addition to both number is:", result)
        finished = True

    except ValueError:  # TODO - add something after except
        print("Please enter a valid integer.")
