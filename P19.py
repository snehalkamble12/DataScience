string = input("Enter a string: ").lower()
text = string.split()
a = {}
for i in text:
    if i not in a:
      a[i] = 0
      print(i)
