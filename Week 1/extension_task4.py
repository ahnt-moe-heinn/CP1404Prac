x = int(input("Enter starting number x: "))
y = int(input("Enter ending number y: "))

print("For 1.")
for i in range(x, y+1, 1):
    if i % 2 == 0:
        print(i, end=' ' + "\n")

print("For 2.")
for i in range(x, y+1, 2):
    if i / 2 != 0:
        print(i, end=' ' + "\n")

print("For 3.")
for i in range(x, y+1, 1):
    print(i*i, end=' ' + "\n")

print("For 4.")