# 35*4.5/100*90
print("Electricity Bill Estimator")
print()
cents = int(input("Enter cents per kWh: "))
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
estimated_bill = ((cents * daily_use)/100) * billing_days
print("Estimated bill: $", estimated_bill)