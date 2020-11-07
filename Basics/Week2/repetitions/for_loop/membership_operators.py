# Ask what phrase they see
print("What phrase do you see?")
phrase = input()

# identifying markings
print("\nRversing... \nThe phrase is: ", end="")

reversed =""

for letter in phrase:
  reversed = letter + reversed

print(reversed)