# for i in range(0, 101, 50):
#     print("{:>4d}".format(i))

# import random
# print(random.randint(5, 20))
# print(random.randrange(3, 10, 2))
# print(random.uniform(2.5, 5.5))
#
# """
# CP1404/CP5632 - Practical
# Capitalist Conrad wants a stock price simulator for a volatile stock.
# The price starts off at $10.00, and, at the end of every day there is
# a 50% chance it increases by 0 to 10%, and
# a 50% chance that it decreases by 0 to 5%.
# If the price rises above $1000, or falls below $0.01, the program should end.
# The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
# """
import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0        #$1
MAX_PRICE = 100.0       #$100
INITIAL_PRICE = 1.0
count = 0

out_file = open("rate.txt", "w")
price = INITIAL_PRICE

print("Starting Price: ${:,.2f}".format(price))
print("Starting Price: ${:,.2f}".format(price), file=out_file)

while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)
    count += 1
    price *= (1 + price_change)
    print("On day {} price is: ${:,.2f}".format(count, price))
    print("On day {} price is: ${:,.2f}".format(count, price), file=out_file)

out_file.close()

# finished = False
# result = 0
# while not finished:
#     try:
#         result = int(input("Enter your marks"))
#         finished = True
#
#     except ValueError:
#         print("Please enter a valid integer")
# print("Valid result is:", result)

# out_file = open("name.txt", "w")
# name = input("What is your name?")
# print(name, file = out_file)
# out_file.close()
#
# in_file = open("name.txt", "r")
# name = in_file.read().strip()
# print("Your name is ", name)
# in_file.close()