# Ask  what phrase they print
print("What phrase do you see?")
phrase = input()

# identtify markings
print("\nreversing...\nThe phrase is", end="")

for position in range(len(phrase) -1, -1, -1 ):
  print(phrase[position], end="")