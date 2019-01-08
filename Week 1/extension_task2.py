print("Electricity Bill Estimator 2.0")
print()

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff = int(input("Which tariff? 11 or 31: "))
# if tariff != 11 and tariff != 31:
#     break
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
if tariff == 11:
    estimated_bill = TARIFF_11 * daily_use * billing_days
elif tariff == 31:
    estimated_bill = TARIFF_31 * daily_use * billing_days
print("Estimated bill: $", estimated_bill)
