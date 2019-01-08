output_file = open("numbers.txt", "r")
first_number = int(output_file.readline())
second_number = int(output_file.readline())
result = first_number + second_number

print(first_number)
print(second_number)
print("Result: ", result)

