# calculate sum of first 100 numbers
print("how many bars should be charged?")
bars_to_charge = int(input())

# Declare a control variable
bars_charged = 0

# display bars_charged
print

while (bars_charged < bars_to_charge):
  bars_charged = bars_charged+1
  print("charhing:", "█" * bars_charged)

print("the bettery is fully charged")