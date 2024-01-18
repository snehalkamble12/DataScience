year=int(input("Enter a year: "))
current_year=2024
if year < current_year :
  print("The year is before current year")
elif year == current_year :
  print("The year is equal to current year")
else:
 print("The year is after current year")
if year % 4 == 0:
  print("The year is a leap year")
else:
  print("The year is not a leap year")
