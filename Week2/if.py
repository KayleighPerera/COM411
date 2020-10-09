print("Please enter your name")
name = input()
print ("your name is {}".format(name))

if (len(name) > 10):
 print("you have a very long name!")
elif (len(name) > 6):
 print("you have a long name")
else:
  print("you have a short name!")

print("end of program")