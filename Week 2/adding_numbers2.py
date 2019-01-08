output_file = open("numbers2.txt", "r")
total = 0
numList = output_file.readlines()
for i in numList:
    new_num = int(i)
    total += new_num
print("Result: ", total)
output_file.close()