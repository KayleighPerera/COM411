# Ask how far they are from the cave
print("How far are we from the cave?")
cave_distance = int (input())

# Display count down
print()

for count in range (cave_distance, 0, -1):
  print(count, "steps remianing")

  print("We have reached the cave!")