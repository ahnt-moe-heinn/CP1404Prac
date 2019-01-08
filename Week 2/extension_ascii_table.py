# LOWER = 33
# UPPER = 128
#
# print("The Range between {} and {}".format(LOWER, UPPER-1))
# for i in range(LOWER, UPPER, 1):
#     print("{}{:>2s}".format(i, chr(i)))

import string

character = input("Enter a character: ")

def count_letters(character):
    count = 0
    for i in character:
        if i.lower() in string.ascii_letters:
            count += 1
    return count
print(count_letters(character))

# decision = letters.isalpha()
# if decision == True:
#     print("Alphabet")
# else:
#     print("Not Alphabet")