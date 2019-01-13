input_file = open("guitars.txt", "w")
fname1 = "Fender Stratocaster"
fname2 = "Gibson L-5 CES"
fname3 = "Line 6 JTV-59"

year1 = "2014"
year2 = "1922"
year3 = "2010"

price1 = 765.40
price2 = 16035.40
price3 = 1512.90

print(fname1,",",year1,",",price1, file=input_file)
print(fname2,",",year2,",",price2, file=input_file)
print(fname3,",",year3,",",price3, file=input_file)

input_file.close()