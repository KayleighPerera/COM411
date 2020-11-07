# start the program
print("Program Strated!")
print("Please enter a standard charcter:")
character = input() 

if (len(character) == 1):
  ascii_value = ord(character)
  print("The ASCII code for {} is {}.".format(character,ascii_value))
else:
  print("invalid charcter!")

print("program ended")