# ask user what they saw and heard
print("what did i hear")
hear = input()

print("what did i see")
see = input()

# determine what message should be displayed
if ( (hear == "grr") and (see == "Two red eyes") ):
  print("\nThere is a scary creature, i should get out of here!")
else:
  print("\nI am a little sacred but i will continue")