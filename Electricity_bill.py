units = int(input("Enter the units: "))
if units <= 100:
  print("No charge")
elif units >= 100 and units<=200:
  total_unit = units-100
  print(total_unit * 5)
else:
  total_charges = 100 * 5
  total_unit = units - 200
  print(total_charges + total_unit * 10)
