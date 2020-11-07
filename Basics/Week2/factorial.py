# Ask user for a number
print("please enter a number?")
number = int(input())

# Calculate factorial
count = 0
total = 1

while (count < number):
  count = count + 1
  total = total * count

print("the factorial is ", total)