while True:
            sales = float(input("Enter sales: $"))
            if 0 < sales < 1000:
                print((sales/100)*10)
            elif sales > 1000:
                print((sales/100)*15)
            elif sales < 0:
                break
