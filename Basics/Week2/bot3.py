# Ask user for direction
print ("please enter the first number.")
first_number = int(input())

print("please enter the second number.")
second_number = int(input())

# Determine which message to display
if (first_number < second_number):
  print("\nThe first number is the smallest.")
elif (first_number > second_number):
  print("\nThe second number is the smallest.")
else:
  print("\nThe numbers are equal")
