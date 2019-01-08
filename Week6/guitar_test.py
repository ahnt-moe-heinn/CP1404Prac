from Week6.do_from_scratch import Guitar
from Week6.car import Car
def main():
    # name = "Gibson L-5 CES"
    # year = 1922
    # cost = 16035.40

    guitar = []
    print("My Guitars!")
    name = input("Name:")
    year = input("Year:")
    cost = input("Cost:")
    guitar.append(Guitar(name, year, cost))
    print("{} ({}) : ${} added.".format(name, year, cost))

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2012, 1512.9)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 95,
                                                      guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(other.name, 5,
                                                      other.get_age()))
    print()
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name,
                                                         True,
                                                         guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(other.name,
                                                         False,
                                                         other.is_vintage()))

main()