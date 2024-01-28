even = []
odd = []

for i in range(6):
  n = int(input("Enter a number: "))
  if n%2 == 0:
    even.append(n)
  else:
    odd.append(n)

d = {}
d['Even'] = even
d['Odd'] = odd
print(d)
