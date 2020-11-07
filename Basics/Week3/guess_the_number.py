import random

print("please enter the minimum value:")
min_value = int(input())

print("please enter the maximum value:")
max_value= int(input())

random_number= random.randrange(min_value, max_value)

print("i am thinking of a number between {} and {}.".format(min_value, max_value))
print("can you guess what it is?")

guess = 0

while(guess != random_number):
  print("please enter a number:")
  guess= int(input())

  if(guess == random_number):
    print("guess higher")
  else:
    print("guess lower")

  print("Game over!")