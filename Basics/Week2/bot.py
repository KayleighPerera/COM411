# Ask user for the direction of brush
print("towards which direction should i paint (up,down, left or right?)")
direction = input()

# Determine which message to display
if (direction == "up"):
  print("\ni am paining in an upward direction")
elif (direction == "down"):
  print("\ni am painting in an downward direction")
elif (direction == "right"):
  print("\ni am painting in a leftward direction")
elif (direction == "left"):
  print("\ni am painting in a rightward direction")
else:
  print("\nnot sure which direction im paining in")