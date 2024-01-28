a = [7, 5, 5, 1, 6, 7, 8, 7, 6]

d={}

for i in a:
  if i not in d:
    d[i] = 1
  else:
    d[i] += 1

for j in d:
  if d[j] == 1:
    print(j)
