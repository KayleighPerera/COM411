# Ask user for sequence and marker
print("please enter a sequence:")
sequence =input()

print("Please enter the characters the marker:")
market= input()

# Fine markers
marker1_position = -1
marker2_position = -1

for position in range(0, len(sequence), 1):
  letter = sequence[position]

 if (letter == marker): 
   if (marker1_position == -1):
            marker1_position = position
        else:
            marker2_position = position
  
# Display result
print ("the distance between the markers is", marker2_position - marker1_position -1)