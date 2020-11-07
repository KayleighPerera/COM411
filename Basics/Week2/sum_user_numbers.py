# Ask user for number
print("How many numbers should i sum up?")
number_to_sum = int(input())

# Declare a control variable
summed = 0

# Display blank lice
print()

# sum number_to_sum
total = 0

while (summed < number_to_sum):
  print ("Please enter number", summed, "of", number_to_sum, ":")
  number = int(input())
  total = total + number
  summed = summed + 1

  # Display result
  print("the answer is", total)