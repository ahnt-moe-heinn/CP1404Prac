import random

SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

UPPER_CASE_CHAR = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_CASE_CHAR = "abcdefghijklmnopqrstuvwxyz"

MIN_LENGTH = 3

MAX_LENGTH = int(input("Enter password maximum length: "))
print(MAX_LENGTH)

upper = int(input("Enter the length of upper case letter: "))
lower = int(input("Enter the length of lower case letter: "))
numeric = int(input("Enter the length of numeric : "))
special_character = int(input("Enter the length of special character: "))

total_count = upper+lower+numeric+special_character

if total_count != MAX_LENGTH:
    print("You inputted password length and total inputted password did not match")
else:
    word = ""
    # while upper != 0 and lower != 0 and numeric != 0 and special_character != 0:
    for i in range(1, 1000):
        ran_generator = random.randint(1, 4)
        if ran_generator == 1:
            while upper != 0:
                word += random.choice(UPPER_CASE_CHAR)
                upper -= 1
        elif ran_generator == 2:
            while lower != 0:
                word += random.choice(LOWER_CASE_CHAR)
                lower -= 1
        elif ran_generator == 3:
            while numeric != 0:
                word += str(random.randint(1, 9))
                numeric -= 1
        elif ran_generator == 4:
            while special_character != 0:
                word += random.choice(SPECIAL_CHARACTERS)
                special_character -= 1
print(word)
