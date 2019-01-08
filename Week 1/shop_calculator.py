num_items = int(input("Number of items: "))
result = 0.0

while num_items <= 0:
    print("Invalid value. Please Enter positive values only")
    num_items = int(input("Enter the number of items: "))

for i in range(1, num_items+1, 1):
    price = float(input("Price of item: "))
    # if price <= 0:
    #     print("Enter the positive number only")
    #     num_items -= 1
    # else:
    result += price

if result > 100.0:
    result = result-0.1 * result
    # result = 0.9 * total

    print("Total price for {} is {}".format(num_items, result))

