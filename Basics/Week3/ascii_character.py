print("Program Started!")
print("Please enter an ASCII code:")
number = abs(int(input()))

if (number >=32 and number <= 126):
  ascii_letter = chr(number)
  print("The charcter represented by the ASCII code {} is {}.".format(number, ascii_letter))
else:
  print("invalid number!")

print("program ended")
