sales = float(input("Enter sales: $"))

if sales < 1000:
    print((sales/100)*10)
elif sales > 1000:
    print((sales/100)*15)
