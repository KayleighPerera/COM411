# Ask user for Fitness advice
print ("how often do you exercise?")
Types_exercise = input()

if ( (Types_exercise == "depends") or (Types_exercise == "sometimes")):
  print ("Keep going")

elif ( (Types_exercise == "daily") or (Types_exercise == "everyday")):
  print ("its recommended to take break days")
elif  ( (Types_exercise == "none") or (Types_exercise == "not active whatsoever") ):
  print ("you must do some sort of excerise everyday even if its 10minutes")

else:
    print ("must fill in")