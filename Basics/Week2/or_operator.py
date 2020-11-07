# Ask user to enter type of adventure
print ("what is the adventure type?")
adventure_type = input()

# detrmine what the type of adventure is
if ( (adventure_type == "scary") or (adventure_type == "short") ):
  print("\nEntering the dark forest!")
elif ( (adventure_type == "safe") or (adventure_type == "long") ):
  print("Taking the safe route")
else:
  print("Not sure which route to take")