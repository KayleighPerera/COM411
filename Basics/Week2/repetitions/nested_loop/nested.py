# ask how many rows and columns they want
print("How many rows would you like")
rows = int(input())

print("how many columns would you like")
columns = int(input())

for row in range (0, rows, 1):
  for column in range(0, columns, 1):
    print(":-)", end= "")
  print()