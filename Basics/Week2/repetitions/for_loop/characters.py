# Ask what markinings they print
print("What strange markings do you see?")
strange_markings = input()

# identify markings
print("\nidentifying....")

for count in range(0, len(strange_markings), 1):
  print("index", count, ":", strange_markings[count])
