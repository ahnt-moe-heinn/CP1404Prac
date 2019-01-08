lines = int(input("Enter Number of lines: "))+1
for i in range (1, lines, 1):
    for j in range(1, i+1, 1):
        print("*", end=' ')
    print()


# for i in range(1, 10, 4):
#     print(i, i * 2, end=" ")
