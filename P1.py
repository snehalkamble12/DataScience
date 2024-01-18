# Display grade as per the marks

grade = int(input("Enter your percentage: "))

if grade > 90 and grade<100:

  print("You got an A!")

elif grade > 80 and grade< 90:

  print("You got a B!")

elif grade > 60 and grade< 80:

  print("You got a C!")

elif grade < 60:

  print("You got a D!")

else:

  print("wrong percentage")
